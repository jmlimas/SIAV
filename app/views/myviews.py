import operator
from django.db.models import Sum, Count, Q
from app.forms import *
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,Group
from django.contrib.auth.decorators import login_required,permission_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms.models import formset_factory
from django.forms.models import BaseInlineFormSet, inlineformset_factory, modelformset_factory

def genera_foliok(avaluo_id,colonia):
    #
    if(len(colonia.split()) > 1):
        primera = colonia.split()[0]
        ultima = colonia.split()[-1]

        folio_k = ultima[:2] + primera[:1] + str(avaluo_id)
        return folio_k
    elif(len(colonia.split()) == 1):
        primera = colonia.split()[0]
        ultima = colonia.split()[-1]

        folio_k =primera[:3] + str(avaluo_id)    
        return folio_k
    else:
        folio_k = ""
        return folio_k

def cantidades():

    avaluos = Avaluo.objects.filter(Estatus__contains='PROCESO', Salida__isnull=True,Visita__isnull=False) | Avaluo.objects.filter(Estatus__contains='DETENIDO', Salida__isnull=True,Visita__isnull=False)
    por_capturar = avaluos.count()
    avaluos = Avaluo.objects.filter(Estatus__contains='PROCESO', Visita__isnull=True, Salida__isnull=True) | Avaluo.objects.filter(Estatus__contains='DETENIDO', Visita__isnull=True, Salida__isnull=True)  
    por_visitar = avaluos.count()
    avaluos = Avaluo.objects.filter(Estatus__contains='PROCESO', Visita__isnull=False, Salida__isnull=True)  
    por_salida = avaluos.count()
    avaluos = Avaluo.objects.filter(Estatus__contains='PROCESO', Salida__isnull=True) | Avaluo.objects.filter(Estatus__contains='DETENIDO', Salida__isnull=True)
    en_proceso = avaluos.count()    
    pendientes = [por_capturar,por_visitar,por_salida,en_proceso]

    return pendientes



@login_required
def home(request):
    avaluos = Avaluo.objects.filter(Estatus__contains='PROCESO', Salida__isnull=True) | Avaluo.objects.filter(Estatus__contains='DETENIDO', Salida__isnull=True)
    cantidad = cantidades()
    return render_to_response('home/home.html',{'avaluos': avaluos,'cantidad':cantidad}, context_instance=RequestContext(request))

@login_required    
def logout_view(request):
    logout(request)
    response = redirect('/SIAV/login/')
    return response
    
@login_required
def facturar(request):
    avaluos = Avaluo.objects.filter(Estatus__contains='CONCLUIDO',Factura__isnull=True,Pagado=False) | Avaluo.objects.filter(Estatus__contains='CONCLUIDO',Factura__isnull=True,Pagado__isnull=True)
    FacturaFormset = modelformset_factory(Avaluo,form=FacturaForm,extra=0)

    if request.method == 'POST':
        factura_formset = FacturaFormset(request.POST,prefix="formas")
        for form in factura_formset:
            if form.is_valid():
                form.save()
        return HttpResponseRedirect('.') 

    else:
        factura_formset = FacturaFormset(queryset=avaluos,prefix="formas")
        example_formset = FacturaFormset(queryset=avaluos,prefix="formas") # ELIMINAR
        cantidad = avaluos.count()
        olist = zip(avaluos,factura_formset)

        suma_de_monto= avaluos.values('Cliente__Cliente').order_by('Cliente').annotate(total=Sum('Importe'))
        total_general = 0.00
        for x in suma_de_monto:
            if not x['total']:
                total_general += 0.00
            else:
                total_general += float(str(x['total']))

        return render_to_response('home/lista_factura.html',{'olist': olist,'cantidad':cantidad,'example_formset':example_formset,'suma_de_monto': suma_de_monto,'total_general': total_general}, context_instance=RequestContext(request))

    
@login_required
def cobrar(request):
    avaluos = Avaluo.objects.filter(Estatus__contains='CONCLUIDO') & Avaluo.objects.exclude(Pagado__contains=1,Factura__isnull=True) & Avaluo.objects.exclude(Factura__isnull=True)
    PagadoFormset = modelformset_factory(Avaluo,form=CobrarForm,extra=0)

    if request.method == 'POST':
        pagado_formset =  PagadoFormset(request.POST,prefix="formas")
        for form in pagado_formset:
            if form.is_valid():
                form.save()
        return HttpResponseRedirect('.') 

    else:
        agrupados = avaluos.values('Factura').annotate(Total=Sum('Importe'))
        pagado_formset = PagadoFormset(queryset=avaluos,prefix="formas")
        example_formset = PagadoFormset(queryset=avaluos,prefix="formas") 
        cantidad = avaluos.count()
        olist = zip(avaluos,pagado_formset)
        
        return render_to_response('home/lista_cobrar.html',{'olist': olist,'cantidad':cantidad,'example_formset':example_formset,'agrupados':agrupados}, context_instance=RequestContext(request))

@login_required
def captura(request):
    #lista_avaluos = Avaluo.objects.all()
    avaluos = Avaluo.objects.filter(Estatus__contains='PROCESO', Salida__isnull=True,Visita__isnull=False) | Avaluo.objects.filter(Estatus__contains='DETENIDO', Salida__isnull=True,Visita__isnull=False)
    cantidad = cantidades()
    return render_to_response('home/captura.html',{'avaluos': avaluos,'cantidad':cantidad}, context_instance=RequestContext(request))

"""
    paginator = Paginator(lista_avaluos, 500)

    page = request.GET.get('page',1)

    try:
        avaluos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        avaluos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        avaluos = paginator.page(paginator.num_pages)
"""    
    
@login_required
def visita(request):
    avaluos = Avaluo.objects.filter(Estatus__contains='PROCESO', Visita__isnull=True, Salida__isnull=True) | Avaluo.objects.filter(Estatus__contains='DETENIDO', Visita__isnull=True, Salida__isnull=True)  
    cantidad = cantidades()
    return render_to_response('home/visita.html',{'avaluos': avaluos,'cantidad':cantidad}, context_instance=RequestContext(request))

@login_required
def salida(request):
    avaluos = Avaluo.objects.filter(Estatus__contains='PROCESO', Visita__isnull=False, Salida__isnull=True)  
    cantidad = cantidades()
    return render_to_response('home/salida.html',{'avaluos': avaluos,'cantidad':cantidad}, context_instance=RequestContext(request))


@login_required
def alta_avaluo(request):

    # Si la forma es enviada...
    cantidad = Avaluo.objects.count()
    if request.method == 'POST':
        # La forma ligada a los datos enviados en el POST
        forma = AltaAvaluo(request.POST)      
        # Todas las reglas de validacion aprobadas
        if forma.is_valid():
            copia_forma = forma
            forma.save()

            reciente = Avaluo.objects.latest('avaluo_id')
            folio_k = genera_foliok(reciente.avaluo_id, reciente.Colonia)
            reciente.FolioK = folio_k
            reciente.save()

            return redirect('/SIAV/alta_avaluo/') # Redirect after POST
    else:
        forma = AltaAvaluo() # An unbound form

    return render_to_response('home/alta_avaluo.html', { 'forma': forma,'cantidad':cantidad, }, context_instance=RequestContext(request))

@login_required
def actualiza_avaluo(request, id):
    if  id == None:
        forma = CapturaAvaluo()
    else:
        avaluo = Avaluo.objects.get(pk = id)
        #colonia = form.cleaned_data['Colonia']
        #avaluo_id = form.cleaned_data.get('avaluo_id')
        colonia = avaluo.Colonia
        avaluo_id = avaluo.avaluo_id
         
        folio_k = genera_foliok(avaluo_id,colonia)

    if request.method == 'POST':
        form = CapturaAvaluo(request.POST, instance=avaluo)
        form.helper.form_action = reverse('actualiza_avaluo', args=[id])
        if form.is_valid():
            obj = form.save(commit=False)
            obj.FolioK = folio_k  
            form.save()
            return redirect('/SIAV/captura/')  
    else:
        form = CapturaAvaluo(instance=avaluo)
    return render_to_response('home/edita_avaluo.html', {'form':form, 'avaluo':avaluo, 'folio_k':folio_k   }, context_instance=RequestContext(request)) 
 
@login_required
def edita_visita(request, id):
    if  id == None:
        forma = VisitaAvaluo()
    else:
        avaluo = Avaluo.objects.get(pk = id)
        form = VisitaAvaluo(instance=avaluo)
        
        colonia = avaluo.Colonia
        avaluo_id = avaluo.avaluo_id
        
        folio_k = genera_foliok(avaluo_id,colonia)

    if request.method == 'POST':
        form = VisitaAvaluo(request.POST, instance=avaluo)
        form.helper.form_action = reverse('edita_visita', args=[id])
        if form.is_valid():
            obj = form.save(commit=False)
            obj.FolioK = folio_k  
            form.save()
            return redirect('/SIAV/visita/')  
    else:
        form = VisitaAvaluo(instance=avaluo)
    return render_to_response('home/edita_visita.html', {'form':form, 'avaluo':avaluo,'folio_k':folio_k   }, context_instance=RequestContext(request))  

@login_required
def edita_salida(request, id):
    if  id == None:
        forma = SalidaAvaluo()
    else:
        avaluo = Avaluo.objects.get(pk = id)
        colonia = avaluo.Colonia
        avaluo_id = avaluo.avaluo_id

        folio_k = genera_foliok(avaluo_id,colonia)

    if request.method == 'POST':
        form = SalidaAvaluo(request.POST, instance=avaluo)
        form.helper.form_action = reverse('edita_salida', args=[id])

        if form.is_valid():
            obj = form.save(commit=False)
            obj.FolioK = folio_k  
            obj.Estatus = 'CONCLUIDO'
            form.save()
            return redirect('/SIAV/salida/')  
    else:
        form = SalidaAvaluo(instance=avaluo)
    return render_to_response('home/edita_salida.html', {'form':form, 'avaluo':avaluo, 'folio_k':folio_k  }, context_instance=RequestContext(request))  
  
@login_required
def guarda_master(request,id):
    if  id == None:
        forma = RespuestaConsultaMaster()
        return render_to_response('home/consultas/consulta_master.html', {'forma': forma }, context_instance=RequestContext(request)) 
    else:
        avaluo = Avaluo.objects.get(pk = id)
        forma = RespuestaConsultaMaster(instance=avaluo)

    if request.method == 'POST':
        avaluo = Avaluo.objects.get(pk = id)
        forma = RespuestaConsultaMaster(request.POST,instance=avaluo)
        forma.helper.form_action = reverse('guarda_master', args=[id])
        if forma.is_valid():
            forma.save()
            return redirect('/SIAV/consulta_master/') 
    return render_to_response('home/consultas/consulta_master.html', { 'forma': forma }, context_instance=RequestContext(request))

@login_required
def consulta_master(request):
    if request.method == 'POST':
        forma = FormaConsultaMaster(request.POST) 
        if forma.is_valid():
            foliok = forma.cleaned_data['FolioK']
            ref = forma.cleaned_data['Referencia']
            calle = forma.cleaned_data['Calle']
            nume = forma.cleaned_data['NumExt']
            numi = forma.cleaned_data['NumInt']
            col = forma.cleaned_data['Colonia']
            mun = forma.cleaned_data['Municipio']
            edo = forma.cleaned_data['Estado']
            tips = forma.cleaned_data['Servicio']
            tipi = forma.cleaned_data['Tipo']
            mes = forma.cleaned_data['Mes']
            anio = forma.cleaned_data['Anio']

            avaluos = Avaluo.objects.all()    

            if foliok:
                avaluos = avaluos.filter(FolioK__icontains=foliok)
            if ref:
                avaluos = avaluos.filter(Referencia__icontains=ref)
            if calle:
                avaluos = avaluos.filter(Calle__icontains=calle)
            if nume:
                avaluos = avaluos.filter(NumExt__icontains=nume)
            if numi:
                avaluos = avaluos.filter(NumInt__icontains=numi)
            if col:
                avaluos = avaluos.filter(Colonia__icontains=col)
            if mun:
                avaluos = avaluos.filter(Municipio__icontains=mun)
            if edo:
                avaluos = avaluos.filter(Estado__icontains=edo)
            if ((tips) and (tips != "N/D")):
                avaluos = avaluos.filter(Servicio__icontains=tips)
            if (tipi):
                avaluos = avaluos.filter(Tipo__Tipo__icontains=tipi)
            if mes and anio:
                inicio = str(anio)+"-"+str(mes)+"-01"
                mes = int(mes)
                if mes % 2 == 00:
                    if mes == 02:
                        dias = "28"
                    else:
                        dias = "31"
                elif mes % 2 != 0:
                    dias ="30"
                fin = str(anio)+"-"+str(mes)+"-"+dias
                avaluos = avaluos.filter(Solicitud__range=(inicio,fin))
            cantidad = avaluos.count()
            return render_to_response('home/consultas/lista_consultaM.html', { 'forma': forma,'avaluos':avaluos,'cantidad':cantidad }, context_instance=RequestContext(request))
    else:
        forma = FormaConsultaMaster()
        return render_to_response('home/consultas/consulta_master.html', { 'forma': forma }, context_instance=RequestContext(request))

@login_required
def consulta_sencilla(request):
    if request.method == 'POST':
        forma = FormaConsultaSencilla(request.POST) 
        if('Buscar' in request.POST):
            if forma.is_valid():
                foliok = forma.cleaned_data['FolioK']
                ref = forma.cleaned_data['Referencia']
                calle = forma.cleaned_data['Calle']
                nume = forma.cleaned_data['NumExt']
                numi = forma.cleaned_data['NumInt']
                col = forma.cleaned_data['Colonia']
                mun = forma.cleaned_data['Municipio']
                edo = forma.cleaned_data['Estado']
                tips = forma.cleaned_data['Servicio']
                tipi = forma.cleaned_data['Tipo']
                mes = forma.cleaned_data['Mes']
                anio = forma.cleaned_data['Anio']

                avaluos = Avaluo.objects.all()    

                if foliok:
                    avaluos = avaluos.filter(FolioK__icontains=foliok)
                if ref:
                    avaluos = avaluos.filter(Referencia__icontains=ref)
                if calle:
                    avaluos = avaluos.filter(Calle__icontains=calle)
                if nume:
                    avaluos = avaluos.filter(NumExt__icontains=nume)
                if numi:
                    avaluos = avaluos.filter(NumInt__icontains=numi)
                if col:
                    avaluos = avaluos.filter(Colonia__icontains=col)
                if mun:
                    avaluos = avaluos.filter(Municipio__icontains=mun)
                if edo:
                    avaluos = avaluos.filter(Estado__icontains=edo)
                if ((tips) and (tips != "N/D")):
                    avaluos = avaluos.filter(Servicio__icontains=tips)
                if tipi:
                    avaluos = avaluos.filter(Tipo__Tipo__icontains=tipi)
                if mes and anio:
                    inicio = str(anio)+"-"+str(mes)+"-01"
                    mes = int(mes)
                    if mes % 2 == 00:
                        if mes == 02:
                            dias = "28"
                        else:
                            dias = "31"
                    elif mes % 2 != 0:
                        dias ="30"
                    fin = str(anio)+"-"+str(mes)+"-"+dias
                    avaluos = avaluos.filter(Solicitud__range=(inicio,fin))
                cantidad = avaluos.count()
                return render_to_response('home/consultas/lista_consultaS.html', { 'forma': forma,'avaluos':avaluos,'cantidad':cantidad }, context_instance=RequestContext(request))
    else:
        forma = FormaConsultaSencilla()
    return render_to_response('home/consultas/consulta_sencilla.html', { 'forma': forma }, context_instance=RequestContext(request))


@login_required
def respuesta_consulta_sencilla(request,id):
        avaluo = Avaluo.objects.get(pk=id)
        return render_to_response('home/consultas/respuesta_consulta_sencilla.html', { 'avaluo': avaluo }, context_instance=RequestContext(request))
   
@login_required
def alta_usuario(request):
  """
  Create a login for a new customer.  
  """
  if request.user.is_staff == False:
    return HttpResponse('Acceso No Autorizado.')

  lForm = AltaUsuario()

  if request.POST:
    lForm = AltaUsuario(request.POST)
    if lForm.is_valid():
      
      lNewUser = User()
      lNewUser.username = lForm.cleaned_data['Usuario']
      lNewUser.first_name = lForm.cleaned_data['Nombre']
      lNewUser.email = lForm.cleaned_data['Correo']
      lNewUser.set_password(lForm.cleaned_data['Contrasena'])
      lNewUser.save()
      
      default_group = Group.objects.get(name=lForm.cleaned_data['Grupo'])
      default_group.user_set.add(lNewUser)
      
      return redirect('/SIAV/lista_usuario/')

  return render_to_response('home/alta_usuario.html', {'form' : lForm}, context_instance=RequestContext(request))
  
@login_required
def lista_usuario(request):
    usuarios = User.objects.all() 
    return render_to_response('home/lista_usuario.html',{'usuarios': usuarios}, context_instance=RequestContext(request))  
    
@login_required    
def alta_valuador(request):
    # Si la forma es enviada...
    cantidad = Valuador.objects.count()
    if request.method == 'POST':
        # La forma ligada a los datos enviados en el POST
        forma = AltaValuador(request.POST)
        # Todas las reglas de validacion aprobadas
        if forma.is_valid(): 
            forma.save()
            return redirect('/SIAV/submitted/') # Redirect after POST
    else:
        forma = AltaValuador() # An unbound form

    return render_to_response('home/alta_valuador.html', { 'forma': forma,'cantidad':cantidad, }, context_instance=RequestContext(request))

@login_required
def lista_valuador(request):
    valuadores = Valuador.objects.all() 
    return render_to_response('home/lista_valuador.html',{'valuadores': valuadores}, context_instance=RequestContext(request))  

@login_required    
def mapas(request):
    
    return render_to_response('home/mapas.html',{}, context_instance=RequestContext(request))

@login_required    
def submitted(request):
    return render_to_response('home/submitted.html', context_instance=RequestContext(request))

import operator
from django.db.models import Q
from app.forms import *
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,Group
from django.contrib.auth.decorators import login_required,permission_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def genera_foliok(avaluo_id,colonia):

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

@login_required
def home(request):
    return render_to_response('home/home.html', context_instance=RequestContext(request))

@login_required    
def logout_view(request):
    logout(request)
    response = redirect('/SIAV/login/')
    return response
    
@login_required
def captura(request):
    #lista_avaluos = Avaluo.objects.all()
    avaluos = Avaluo.objects.filter(Estatus__contains='PROCESO') | Avaluo.objects.filter(Estatus__contains='DETENIDO')
    cantidad = avaluos.count()
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
    avaluos = Avaluo.objects.filter(Estatus__contains='PROCESO', Visita__isnull=True) | Avaluo.objects.filter(Estatus__contains='DETENIDO')  
    return render_to_response('home/visita.html',{'avaluos': avaluos}, context_instance=RequestContext(request))

@login_required
def salida(request):
    avaluos = Avaluo.objects.filter(Estatus__contains='PROCESO', Visita__isnull=False)  
    return render_to_response('home/salida.html',{'avaluos': avaluos}, context_instance=RequestContext(request))


@login_required
def alta_avaluo(request):

    # Si la forma es enviada...
    cantidad = Avaluo.objects.count()
    if request.method == 'POST':
        # La forma ligada a los datos enviados en el POST
        forma = AltaAvaluo(request.POST)      
        # Todas las reglas de validacion aprobadas
        if forma.is_valid():
            return redirect('/SIAV/submitted/') # Redirect after POST
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
            form.save()
            return redirect('/SIAV/salida/')  
    else:
        form = SalidaAvaluo(instance=avaluo)
    return render_to_response('home/edita_salida.html', {'form':form, 'avaluo':avaluo, 'folio_k':folio_k  }, context_instance=RequestContext(request))  
  
@login_required
def consulta_master(request,id=0):
    if ((id != 0) & (request.method != 'POST')):
        avaluo = Avaluo.objects.get(pk=id)
        forma = RespuestaConsultaMaster(instance=avaluo)
        return render_to_response('home/consultas/consulta_master.html', { 'forma': forma }, context_instance=RequestContext(request))
    if request.method == 'POST':
        forma = FormaConsultaMaster(request.POST) 
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
                ini = forma.cleaned_data['Inicial']
                fin = forma.cleaned_data['Final']
                tips = forma.cleaned_data['Servicio']
                tipi = forma.cleaned_data['Tipo']

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
                if ((tips)):
                    avaluos = avaluos.filter(Tipo__icontains=tipi)
                if ini and fin:
                    avaluos = avaluos.filter(Solicitud__range=(ini,fin))

                #forma = ConsultaMaster(instance=avaluo)
                return render_to_response('home/consultas/lista_consultaM.html', { 'forma': forma,'avaluos':avaluos }, context_instance=RequestContext(request))

        elif('Guardar' in request.POST):
            if forma.is_valid():
                foliok = forma.cleaned_data['FolioK']
                avaluo = Avaluo.objects.get(FolioK=foliok)
                forma = RespuestaConsultaMaster(request.POST,instance=avaluo)
                forma.save()
                return redirect('/SIAV/consulta_master/') 
    else:
        forma = FormaConsultaMaster()
    return render_to_response('home/consultas/consulta_master.html', { 'forma': forma }, context_instance=RequestContext(request))
     
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

import os
from django.utils import timezone
import datetime
from datetime import date
from django.conf.urls.defaults import *
from django.db.models import Sum, Count, Q
from app.forms import *
from app.haversine import *
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from django.contrib.admin.views.decorators import staff_member_required
from django.core.files import File
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from io import FileIO, BufferedWriter


current_directory = os.path.dirname(os.path.abspath(__file__))


#   Recibe el id y la colonia.
def genera_foliok(avaluo_id, colonia):
    #Generar el FolioK
    if(len(colonia.split()) > 1):
        primera = colonia.split()[0]
        ultima = colonia.split()[-1]

        folio_k = ultima[:2] + primera[:1] + str(avaluo_id)
        return folio_k
    elif(len(colonia.split()) == 1):
        primera = colonia.split()[0]
        ultima = colonia.split()[-1]

        folio_k = primera[:3] + str(avaluo_id)
        return folio_k
    else:
        folio_k = ""
        return folio_k


#   Metodo para contar los avaluos en cada seccion.
def cantidades():

    #Conteo avaluos de Captura
    avaluos = Avaluo.objects.filter(Estatus__contains='PROCESO', Salida__isnull=True, Visita__isnull=False) | Avaluo.objects.filter(Estatus__contains='DETENIDO', Salida__isnull=True, Visita__isnull=False)
    por_capturar = avaluos.count()
    #Conteo avaluos de Visita
    avaluos = Avaluo.objects.filter(Estatus__contains='PROCESO', Visita__isnull=True, Salida__isnull=True) | Avaluo.objects.filter(Estatus__contains='DETENIDO', Visita__isnull=True, Salida__isnull=True)
    por_visitar = avaluos.count()
    #Conteo avaluos de Salida
    avaluos = (Avaluo.objects
               .filter(Estatus='PROCESO')
               .filter(Q(Visita__isnull=False))
               .filter(Q(Salida__isnull=True)))

    avaluos = (avaluos.exclude(Valor=0.00)
               # .exclude(Q(Valor__isnull=True))
               # .exclude(Q(Referencia__isnull=True))
                .exclude(Q(Mterreno__isnull=True))
               # .exclude(Q(Importe__isnull=True))
                .exclude(Q(Mconstruccion__isnull=True))
                #.exclude(Q(Valor__exact=''))
                )
    por_salida = avaluos.count()
    avaluos = Avaluo.objects.filter(Estatus__contains='PROCESO', Salida__isnull=True) | Avaluo.objects.filter(Estatus__contains='DETENIDO', Salida__isnull=True)
    en_proceso = avaluos.count()
    pendientes = [por_capturar, por_visitar, por_salida, en_proceso]

    return pendientes


#   Vista de la pagina inicial (Muestra avaluos en proceso)
@login_required
def home(request):
    avaluos = Avaluo.objects.filter(Estatus__contains='PROCESO', Salida__isnull=True) | Avaluo.objects.filter(Estatus__contains='DETENIDO', Salida__isnull=True)
    avaluos = avaluos.order_by('-Solicitud')
    cantidad = cantidades()
    return render_to_response('home/home.html', {'avaluos': avaluos, 'cantidad': cantidad}, context_instance=RequestContext(request))


#   Vista para cerrar sesion
@login_required
def logout_view(request):
    logout(request)
    response = redirect('/SIAV/login/')
    return response


#   Vista de facturacion.
@staff_member_required
def facturar(request):
    avaluos = (Avaluo.objects
               .filter(Estatus='CONCLUIDO')
               .filter(Q(Salida__isnull=False))
               .filter(Q(Factura='') | Q(Factura__isnull=True))
               .filter(Q(Pagado=False) | Q(Pagado__isnull=True)))
    avaluos = avaluos.order_by('-Salida')
    FacturaFormset = modelformset_factory(Avaluo, form=FacturaForm, extra=0)

    if request.method == 'POST':
        factura_formset = FacturaFormset(request.POST, prefix="formas")
        for form in factura_formset:
            if form.is_valid():
                form.save()
        return HttpResponseRedirect('.')

    else:
        factura_formset = FacturaFormset(queryset=avaluos, prefix="formas")
        example_formset = FacturaFormset(queryset=avaluos, prefix="formas")
        cantidad = avaluos.count()
        olist = zip(avaluos, factura_formset)

        suma_de_monto = avaluos.values('Cliente__Cliente').order_by('Cliente').annotate(total=Sum('Importe'))
        total_general = 0.00
        for x in suma_de_monto:
            if not x['total']:
                total_general += 0.00
                x['Total'] = 0.00
            else:
                total_general += float(str(x['total']))

        return render_to_response('home/lista_factura.html', {'olist': olist, 'cantidad': cantidad, 'example_formset': example_formset, 'suma_de_monto': suma_de_monto, 'total_general': total_general}, context_instance=RequestContext(request))


#   Vista que se encarga de liquidar las facturas ya pagadas
#   Cambiando el estado Pagado de los avaluos de 0 a 1
@staff_member_required
def liquidar(request):
    avaluos = (Avaluo.objects
               .filter(Estatus='CONCLUIDO')
               .filter(Q(Factura__isnull=False))
               .filter(Q(Pagado=0) | Q(Pagado__isnull=True))
               .exclude(Q(Factura__exact='')))
    if request.method == 'POST':
        facturas_pagadas = request.POST.getlist('facturas_pagadas')
        (Avaluo.objects
            .filter(Factura__in=facturas_pagadas)
            .filter(Q(Pagado=0) | Q(Pagado__isnull=True))
            .update(Pagado=True))
        return HttpResponseRedirect('.')
    else:
        agrupados = avaluos.values('Factura', 'Cliente__Cliente').annotate(Total=Sum('Importe'), Cantidad=Count('Factura'))

        cantidad = avaluos.count()
        total_general = 0.00
        for x in agrupados:
            if not x['Total']:
                total_general += 0.00
                x['Total'] = 0.00
            else:
                total_general += float(str(x['Total']))
        return render_to_response('home/lista_cobrar.html', {'total_general': total_general, 'cantidad': cantidad, 'agrupados': agrupados}, context_instance=RequestContext(request))


#   Vista para generar estadisticos en Highcharts
#   Se planea segmentar para generar diferentes clases de estadistico.
@staff_member_required
def estadistico(request, anio=2013):
    anios = Avaluo.objects.all().dates('Salida', 'year')
    avaluos = Avaluo.objects.extra(select={'month': 'extract( month from Salida )'}).values('month').filter(Salida__year=anio).order_by('month').annotate(dcount=Count('Solicitud'), Total=Sum('Importe'))
    cliente = Avaluo.objects.filter(Salida__year=anio).values('Cliente__Cliente').annotate(Total=Sum('Importe'), Cantidad=Count('Cliente'))
    tiempo_respuesta = Avaluo.objects.filter(Salida__year=anio).values('Depto__Depto','Solicitud','Salida').annotate(Total=Sum('Importe'), Cantidad=Count('Cliente'))
    monto_todos_anios = Avaluo.objects.extra(select={'year': 'extract( year from Salida )'}).values('year').annotate(Total=Sum('Importe')).order_by('year')

    total_general = 0.00
    total_avaluos = 0
    for x in avaluos:
        if not x['Total']:
            total_general += 0.00
            total_avaluos += x['dcount']
            x['Total'] = 0.00
        else:
            total_general += float(str(x['Total']))
            total_avaluos += x['dcount']
    totales = [total_avaluos, total_general]
    return render_to_response('home/estadistico.html', {'avaluos': avaluos, 'totales': totales, 'anio': anio, 'anios': anios, 'monto_todos_anios': monto_todos_anios, 'cliente': cliente, 'tiempo_respuesta': tiempo_respuesta}, context_instance=RequestContext(request))


@login_required
def captura(request):
    #lista_avaluos = Avaluo.objects.all()
    avaluos = Avaluo.objects.filter(Estatus__contains='PROCESO', Salida__isnull=True, Visita__isnull=False) | Avaluo.objects.filter(Estatus__contains='DETENIDO', Salida__isnull=True, Visita__isnull=False)
    avaluos = avaluos.order_by('-Solicitud')
    cantidad = cantidades()
    return render_to_response('home/captura.html', {'avaluos': avaluos, 'cantidad': cantidad}, context_instance=RequestContext(request))


@login_required
def visita(request):
    avaluos = Avaluo.objects.filter(Estatus__contains='PROCESO', Visita__isnull=True, Salida__isnull=True) | Avaluo.objects.filter(Estatus__contains='DETENIDO', Visita__isnull=True, Salida__isnull=True)
    avaluos = avaluos.order_by('-Solicitud')
    cantidad = cantidades()
    return render_to_response('home/visita.html', {'avaluos': avaluos, 'cantidad': cantidad}, context_instance=RequestContext(request))


@login_required
def salida(request):
    avaluos = (Avaluo.objects
               .filter(Estatus='PROCESO')
               .filter(Q(Visita__isnull=False))
               .filter(Q(Salida__isnull=True)))

    avaluos = (avaluos.exclude(Valor=0.00)
                .exclude(Q(Valor__isnull=True))
                .exclude(Q(Referencia__isnull=True))
                .exclude(Q(Mterreno__isnull=True))
                .exclude(Q(Importe__isnull=True))
                .exclude(Q(Mconstruccion__isnull=True))
                #.exclude(Q(Valor__exact=''))
                )



    avaluos = avaluos.order_by('-Solicitud')
    cantidad = cantidades()
    return render_to_response('home/salida.html', {'avaluos': avaluos, 'cantidad': cantidad}, context_instance=RequestContext(request))

def salida_efectiva(request, id):
    avaluo = Avaluo.objects.get(avaluo_id=id)
    avaluo.Salida = datetime.date.isoformat(date.today())
    avaluo.Estatus = 'CONCLUIDO'
    avaluo.save()
    return salida(request)


@login_required
def alta_avaluo(request):

    # Si la forma es enviada...
    cantidad = cantidades()
    if request.method == 'POST':
        # La forma ligada a los datos enviados en el POST
        forma = AltaAvaluo(request.POST)
        # Todas las reglas de validacion aprobadas
        if forma.is_valid():
            forma.save()

            reciente = Avaluo.objects.latest('avaluo_id')
            folio_k = genera_foliok(reciente.avaluo_id, reciente.Colonia)
            reciente.FolioK = folio_k
            reciente.save()

            return redirect('/SIAV/alta_avaluo/')  # Redirect after POST
    else:
        forma = AltaAvaluo()  # An unbound form

    return render_to_response('home/alta_avaluo.html', {'forma': forma, 'cantidad': cantidad, }, context_instance=RequestContext(request))


@login_required
def actualiza_avaluo(request, id):
    if id is None:
        form = CapturaAvaluo()
    else:
        avaluo = Avaluo.objects.get(pk=id)
        colonia = avaluo.Colonia
        avaluo_id = avaluo.avaluo_id

        folio_k = genera_foliok(avaluo_id, colonia)

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
    decimal = decimal_conversion(avaluo)
    cercanos = find_closest(avaluo)
    imagenes = ImagenAvaluo.objects.filter(avaluo = avaluo.avaluo_id)[:3]
    archivos = ArchivoAvaluo.objects.filter(avaluo = avaluo.avaluo_id)
    return render_to_response('home/edita_avaluo.html', {'form': form, 'avaluo': avaluo, 'decimal': decimal, 'cercanos': cercanos,'imagenes': imagenes,'archivos': archivos, 'folio_k': folio_k}, context_instance=RequestContext(request))


@login_required
def edita_visita(request, id):

    if id is None:
        form = VisitaAvaluo()
    else:
        avaluo = Avaluo.objects.get(pk=id)
        form = VisitaAvaluo(instance=avaluo)

        colonia = avaluo.Colonia
        avaluo_id = avaluo.avaluo_id

        folio_k = genera_foliok(avaluo_id, colonia)

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
    decimal = decimal_conversion(avaluo)
    cercanos = find_closest(avaluo)
    imagenes = ImagenAvaluo.objects.filter(avaluo = avaluo.avaluo_id)[:3]
    return render_to_response('home/edita_visita.html', {'form': form, 'avaluo': avaluo, 'decimal': decimal, 'cercanos': cercanos,'imagenes': imagenes, 'folio_k': folio_k}, context_instance=RequestContext(request))


@login_required
def edita_salida(request, id):
    if id is None:
        form = SalidaAvaluo()
    else:
        avaluo = Avaluo.objects.get(pk=id)
        colonia = avaluo.Colonia
        avaluo_id = avaluo.avaluo_id
        folio_k = genera_foliok(avaluo_id, colonia)

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
    return render_to_response('home/edita_salida.html', {'form': form, 'avaluo': avaluo, 'folio_k': folio_k}, context_instance=RequestContext(request))


@staff_member_required
def guarda_master(request, id):
    if id is None:
        forma = RespuestaConsultaMaster()
        imagenes = ImagenAvaluo.objects.none()
        return render_to_response('home/consultas/respuesta_consulta_master.html', {'forma': forma, 'imagenes': imagenes}, context_instance=RequestContext(request))
    else:
        avaluo = Avaluo.objects.get(pk=id)
        imagenes = ImagenAvaluo.objects.filter(avaluo=id)[:3]

        forma = RespuestaConsultaMaster(instance=avaluo)

    if request.method == 'POST':
        avaluo = Avaluo.objects.get(pk=id)

        colonia = avaluo.Colonia
        avaluo_id = avaluo.avaluo_id

        forma = RespuestaConsultaMaster(request.POST, instance=avaluo)
        forma.helper.form_action = reverse('guarda_master', args=[id])
        folio_k = genera_foliok(avaluo_id, colonia)
        if forma.is_valid():
            obj = forma.save(commit=False)
            obj.FolioK = folio_k
            forma.save()
            return redirect('/SIAV/consulta_master/')
    return render_to_response('home/consultas/respuesta_consulta_master.html', {'forma': forma, 'avaluo': avaluo, 'imagenes': imagenes}, context_instance=RequestContext(request))


@staff_member_required
def consulta_master(request):
    if request.is_ajax():
        foliok = request.GET.get('foliok', '')
        ref = request.GET.get('ref', '')
        calle = request.GET.get('calle', '')
        col = request.GET.get('col', '')
        factura = request.GET.get('factura', '')
        edo = request.GET.get('edo', '')
        mun = request.GET.get('mun', '')
        cli = request.GET.get('cli', '')
        dep = request.GET.get('dep', '')
        imp = request.GET.get('imp', '')
        tipo = request.GET.get('tipo', '')
        mes = request.GET.get('mes', '')
        anio = request.GET.get('anio', '')

        results = Avaluo.objects.all()
        if foliok:
            results = results.filter(Q(FolioK__contains=foliok))
        if ref:
            results = results.filter((Q(Referencia__contains=ref)))
        if calle:
            results = results.filter((Q(Calle__contains=calle)))    
        if col:
            results = results.filter((Q(Colonia__contains=col)))                 
        if factura:
            results = results.filter((Q(Factura__contains=factura)))
        if edo:
            results = results.filter((Q(Estado=edo)))    
        if mun:
            results = results.filter((Q(Municipio=mun)))
        if cli:
            results = results.filter((Q(Cliente=cli)))    
        if dep:
            results = results.filter((Q(Depto=dep)))        
        if imp:
            results = results.filter((Q(Importe__icontains=imp)))  
        if tipo:
            results = results.filter((Q(Tipo=tipo)))
        if anio:
            results = results.filter(Solicitud__year=anio)
            if mes and anio:
                inicio = str(anio)+"-"+str(mes)+"-01"
                mes = int(mes)
                if mes % 2 == 00:
                    if mes == 02:
                        dias = "28"
                    else:
                        dias = "30"
                elif mes % 2 != 0:
                    dias = "31"
                fin = str(anio)+"-"+str(mes)+"-"+dias
                results = results.filter(Solicitud__range=(inicio, fin))

        data = {'results': results}
        return render_to_response('home/consultas/results.html', data, context_instance=RequestContext(request))
    else:
        forma = FormaConsultaMaster()
        return render_to_response('home/consultas/consulta_master.html', {'forma': forma}, context_instance=RequestContext(request))


@login_required
def consulta_sencilla(request):
    cantidad = cantidades()
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
                    avaluos = avaluos.filter(Municipio=mun)
                if edo:
                    avaluos = avaluos.filter(Estado=edo)
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
                            dias = "30"
                    elif mes % 2 != 0:
                        dias = "31"
                    fin = str(anio)+"-"+str(mes)+"-"+dias
                    avaluos = avaluos.filter(Solicitud__range=(inicio, fin))
                cantidad = avaluos.count()
                avaluos = avaluos.order_by('-Solicitud')
                return render_to_response('home/consultas/lista_consultaS.html', {'forma': forma, 'avaluos': avaluos, 'cantidad': cantidad}, context_instance=RequestContext(request))
    else:
        forma = FormaConsultaSencilla()
        cantidad = cantidades()
    return render_to_response('home/consultas/consulta_sencilla.html', {'forma': forma, 'cantidad': cantidad}, context_instance=RequestContext(request))


@login_required
def respuesta_consulta_sencilla(request, id):
        avaluo = Avaluo.objects.get(pk=id)
        return render_to_response('home/consultas/respuesta_consulta_sencilla.html', {'avaluo': avaluo}, context_instance=RequestContext(request))


@login_required
def alta_usuario(request):

    #  Crear login para un nuevo usuario.

    if request.user.is_staff is False:
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

    return render_to_response('home/alta_usuario.html', {'form': lForm}, context_instance=RequestContext(request))


#   Muestra la lista de usuarios registrados
@login_required
def lista_usuario(request):
    usuarios = User.objects.all()
    return render_to_response('home/lista_usuario.html', {'usuarios': usuarios}, context_instance=RequestContext(request))


#   Vista para dar de alta a un valuador.
#   Se contempla incluir esta funcionalidad en el admin
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
            return redirect('/SIAV/submitted/')  # Redirect after POST
    else:
        forma = AltaValuador()  # An unbound form

    return render_to_response('home/alta_valuador.html', {'forma': forma, 'cantidad': cantidad}, context_instance=RequestContext(request))


@login_required
def lista_valuador(request):
    valuadores = Valuador.objects.all()
    return render_to_response(current_directory+'/../../media', {'valuadores': valuadores}, context_instance=RequestContext(request))


@login_required
def mapas(request):
#    path = default_storage.save(d, ContentFile('new_content.html'))
    
    avaluo = Avaluo.objects.order_by('?')[0]
    decimal = decimal_conversion(avaluo)
    cercanos = find_closest(avaluo)
    todos = Avaluo.objects.all().order_by('?')[:100]
    imagenes = ImagenAvaluo.objects.all()
    return render_to_response('home/mapas.html', {'avaluo': avaluo, 'todos': todos, 'imagenes': imagenes,'decimal': decimal, 'cercanos': cercanos}, context_instance=RequestContext(request))


@login_required
def submitted(request):
    return render_to_response('home/submitted.html', context_instance=RequestContext(request))


def pdf_view(avaluo_id):
    archivo = ArchivoAvaluo.objects.filter(avaluo = avaluo.avaluo_id)
    response = HttpResponse(archivo, mimetype='application/pdf')
    response['Content-Disposition'] = 'inline;filename=some_file.pdf'
    return response
    pdf.closed

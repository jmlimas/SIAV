# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from ficha.forms import *
from ficha.models import *
from django.forms.models import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from app.haversine import *

muncipio = 0
def elimina_imagen(request,folio,imagen_id):
    ImagenFicha.objects.filter(imagen_id=imagen_id).delete()
    return captura_ficha(request,folio)

def investigacion_mercado(request):
    investigaciones = Investigacion_Mercado.objects.all()
    return render_to_response('home/ficha/investigacion_mercado.html', {'investigaciones': investigaciones}, context_instance=RequestContext(request))

def captura_ficha(request, folio=None):

    ficha = Ficha_Tecnica.objects.get(folio=folio)
    #invest_mercado = (Investigacion_Mercado.objects.filter(ficha_id=1))
    IMForsmet = inlineformset_factory(Ficha_Tecnica,Investigacion_Mercado, form=InvestigacionMercado, extra=0, can_delete=True)
    VUForsmet = inlineformset_factory(Ficha_Tecnica,Valores_Unitarios, form=ValoresUnitarios, extra=0, can_delete=True)
    if request.method != 'POST':
        if folio is None:
            form = CapturaFicha()
            valor_propuesto = ValorPropuesto()
            im_formset = IMForsmet()
            vu_formset = VUForsmet()
        else:  
            form = CapturaFicha(instance=ficha)
            invest_mercado = (Investigacion_Mercado.objects.filter(ficha_id=folio).count())
            valores_unitarios = (Valores_Unitarios.objects.filter(ficha_id=folio).count())

            if invest_mercado == 3:
                im_formset = IMForsmet(instance=ficha)
            elif invest_mercado > 3:
                Investigacion_Mercado.objects.filter(ficha_id=folio).delete()
                return HttpResponse("<h1>Hubo un error en tu solicitud, porfavor intenta nuevamente</h1>")
            else:
                IMForsmet = inlineformset_factory(Ficha_Tecnica,Investigacion_Mercado, form=InvestigacionMercado, extra=3, can_delete=True)
                im_formset = IMForsmet()  

            if valores_unitarios == 3:
                vu_formset = VUForsmet(instance=ficha)
            elif valores_unitarios > 3:
                Valores_Unitarios.objects.filter(ficha_id=folio).delete()
                return HttpResponse("<h1>Hubo un error en tu solicitud, porfavor intenta nuevamente</h1>")
            else:
                VUForsmet = inlineformset_factory(Ficha_Tecnica,Valores_Unitarios, form=ValoresUnitarios, extra=3, can_delete=True)     
                vu_formset = VUForsmet()     

            valor_propuesto = ValorPropuesto(instance=ficha)
    if request.method == 'POST':
        form = CapturaFicha(request.POST, instance=ficha)
        im_formset = IMForsmet(request.POST, instance=ficha)
        vu_formset = VUForsmet(request.POST, instance=ficha)
        valor_propuesto = ValorPropuesto(request.POST, instance=ficha)
        #form.helper.form_action = reverse('captura_ficha', args=[id])
        if form.is_valid() and valor_propuesto.is_valid() and im_formset.is_valid() and vu_formset.is_valid():
            form.save()
            valor_propuesto.save()
            im_formset.save()
            vu_formset.save()
            return redirect('/SIAV/captura_ficha/'+folio)
        else:
            return HttpResponse("error")
    else:
        print 'pendiente'
        form = CapturaFicha(instance=ficha)
        valor_propuesto = ValorPropuesto(instance=ficha)
        imagenes = ImagenFicha.objects.filter(ficha = ficha.folio)[:5]
    cercanos = find_closest_ficha(ficha)
    decimal = decimal_conversion(ficha)
    return render_to_response('home/ficha/captura_ficha.html', {'form': form, 'ficha': ficha,'valor_propuesto':valor_propuesto,'im_formset':im_formset,'vu_formset':vu_formset,'imagenes':imagenes,'decimal':decimal,'cercanos':cercanos}, context_instance=RequestContext(request))

def simple_ficha(request, folio=None):

    ficha = Ficha_Tecnica.objects.get(folio=folio)
    form = CapturaFicha(instance=ficha)
    imagenes = ImagenFicha.objects.filter(ficha = ficha.folio)[:4]
    im_formset = Investigacion_Mercado.objects.filter(ficha_id=folio)
    vu_formset = Valores_Unitarios.objects.filter(ficha_id=folio)
    return render_to_response('home/ficha/reports/ficha1.html', {'form':form, 'ficha': ficha,'im_formset':im_formset,'vu_formset':vu_formset,'imagenes':imagenes}, context_instance=RequestContext(request))

def resumen_ficha(request, municipio=986, region=None):

    ficha = Ficha_Tecnica.objects.filter(region=region,municipio=municipio)
    #form = CapturaFicha(instance=ficha)
    #imagenes = ImagenFicha.objects.filter(ficha = ficha.folio)[:4]
    #im_formset = Investigacion_Mercado.objects.filter(ficha_id=folio)
    #vu_formset = Valores_Unitarios.objects.filter(ficha_id=folio)
    region = ficha.values('region').annotate(dcount=Count('region')).order_by('region')
    return render_to_response('home/ficha/reports/ficha2.html', {'ficha': ficha}, context_instance=RequestContext(request))


def ficha(request, municipio=986):
    municipio = Municipio.objects.get(municipio_id=municipio)
    fichas = Ficha_Tecnica.objects.filter(municipio_id=municipio)
    fichas = fichas.order_by('folio')
    cantidad = fichas.count()
    region = fichas.values('region','municipio').annotate(dcount=Count('region')).order_by('region')

    return render_to_response('home/ficha/ficha.html', {'fichas': fichas, 'cantidad': cantidad,'municipio':municipio,'region':region}, context_instance=RequestContext(request))


def ficha_preliminar(request):
    fichas = Ficha_Tecnica.objects.all()
    fichas = fichas.order_by('folio')
    cantidad = fichas.count()
    return render_to_response('home/ficha/ficha_preliminar.html', {'fichas': fichas, 'cantidad': cantidad}, context_instance=RequestContext(request))


# -*- coding: utf-8 -*-
from app.models import Avaluo
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render_to_response, redirect

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



def show_orden_visita(request):
    lista_visitado = request.GET.getlist('avaluo_visitado')
    avaluos_visitados = Avaluo.objects.filter(FolioK__in=lista_visitado)
    avaluo = avaluos_visitados[0]
    return render_to_response('reports/orden_visita.html',{'avaluo':avaluo,'avaluos_visitados':avaluos_visitados}, context_instance=RequestContext(request))

def show_visita_pdf(request, id):
    avaluo= Avaluo.objects.get(pk=id)

    colonia = avaluo.Colonia
    avaluo_id = avaluo.avaluo_id
        
    folio_k = genera_foliok(avaluo_id,colonia)

    if(avaluo.Tipo_id == 1):
        return render_to_response('reports/visita_terreno.html',{'folio_k':folio_k,'avaluo':avaluo}, context_instance=RequestContext(request))
    elif(avaluo.Tipo_id == 2):
        return render_to_response('reports/visita_casa.html',{'folio_k':folio_k,'avaluo':avaluo}, context_instance=RequestContext(request))
    elif(avaluo.Tipo_id == 3):
        return render_to_response('reports/visita_casa.html',{'folio_k':folio_k,'avaluo':avaluo}, context_instance=RequestContext(request))
    elif(avaluo.Tipo_id == 4):
        return render_to_response('reports/visita_nave.html',{'folio_k':folio_k,'avaluo':avaluo}, context_instance=RequestContext(request))
    elif(avaluo.Tipo_id == 5):
        return render_to_response('reports/visita_nave.html',{'folio_k':folio_k,'avaluo':avaluo}, context_instance=RequestContext(request))
    elif(avaluo.Tipo_id == 6):
        return render_to_response('reports/visita_nave.html',{'folio_k':folio_k,'avaluo':avaluo}, context_instance=RequestContext(request))
    else:
        return HttpResponseNotFound('<h1>No se encontró el reporte.</h1>')
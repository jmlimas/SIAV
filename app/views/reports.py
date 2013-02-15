# -*- coding: utf-8 -*-
from app.models import Avaluo
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render_to_response, redirect

def show_visita_pdf(request, id):
    avaluo= Avaluo.objects.get(pk=id)
    if(avaluo.Tipo_id == 1):
        return render_to_response('reports/visita_terreno.html',{'avaluo':avaluo}, context_instance=RequestContext(request))
    elif(avaluo.Tipo_id == 2):
        return render_to_response('reports/visita_casa.html',{'avaluo':avaluo}, context_instance=RequestContext(request))
    elif(avaluo.Tipo_id == 3):
        return render_to_response('reports/visita_casa.html',{'avaluo':avaluo}, context_instance=RequestContext(request))
    elif(avaluo.Tipo_id == 4):
        return render_to_response('reports/visita_nave.html',{'avaluo':avaluo}, context_instance=RequestContext(request))
    elif(avaluo.Tipo_id == 5):
        return render_to_response('reports/visita_nave.html',{'avaluo':avaluo}, context_instance=RequestContext(request))
    elif(avaluo.Tipo_id == 6):
        return render_to_response('reports/visita_nave.html',{'avaluo':avaluo}, context_instance=RequestContext(request))
    else:
        return HttpResponseNotFound('<h1>No se encontró el reporte.</h1>')
import json
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

def test(request):
        return render_to_response('home/ajax_test.html',{}, context_instance=RequestContext(request))

def get_colonias(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        colonias = Avaluo.objects.filter(Colonia__contains = q.upper()).values_list('Colonia', flat=True).distinct()[:20]
        results = []
        for colonia in colonias:
            colonia_json = {}
            colonia_json['label'] = colonia
            colonia_json['value'] = colonia
            results.append(colonia_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def get_municipios(request):
    if request.is_ajax():
        q = request.GET.get('id', '')
        print q
        municipios = Municipio.objects.filter(estado_id = q )
        results = []
        for municipio in municipios:
            municipio_json = {}
            municipio_json['optionValue'] = municipio.municipio_id
            municipio_json['optionDisplay'] = municipio.Nombre
            results.append(municipio_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def get_deptos(request):
    if request.is_ajax():
        q = request.GET.get('id', '')
        print q
        deptos = Depto.objects.filter(cliente_id = q ,is_active=True)
        results = []
        for depto in deptos:
            depto_json = {}
            depto_json['optionValue'] = depto.depto_id
            depto_json['optionDisplay'] = depto.Depto
            results.append(depto_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


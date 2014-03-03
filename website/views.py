from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
# Create your views here.

def index(request):
    return render_to_response('ericka/index.html', {}, context_instance=RequestContext(request))

def servicios(request):
    return render_to_response('ericka/services.html', {}, context_instance=RequestContext(request))

def faq(request):
    return render_to_response('ericka/faq.html', {}, context_instance=RequestContext(request))

def contacto(request):
    return render_to_response('ericka/contact.html', {}, context_instance=RequestContext(request))

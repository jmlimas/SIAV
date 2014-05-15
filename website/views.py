#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from website.forms import FormaContacto
from django.core.mail import send_mail

# Create your views here.

def index(request):
    return render_to_response('ericka/index.html', {}, context_instance=RequestContext(request))

def servicios(request):
    return render_to_response('ericka/services.html', {}, context_instance=RequestContext(request))

def faq(request):
    return render_to_response('ericka/faq.html', {}, context_instance=RequestContext(request))

def contacto(request):
	forma = FormaContacto()
	if request.method == 'POST':
	    # La forma ligada a los datos enviados en el POST
	    forma = FormaContacto(request.POST)
	    # Todas las reglas de validacion aprobadas
	    if forma.is_valid():
	    	#send_mail('Contacto Alluxi',forma.cleaned_data['Mensaje'],['gusreyes01@gmail.com',], fail_silently=False)
	        send_mail('Contacto Alluxi', forma.cleaned_data['Mensaje'], 'hola@gmail.com', ['gusreyes01@gmail.com'], fail_silently=False)
	        return HttpResponse('Enviado')  # Redirect after POST
	    else:
			return HttpResponse('Envío Fallido')
	else:
		forma = FormaContacto()  # An unbound form
		return render_to_response('ericka/contact.html', {'forma':forma}, context_instance=RequestContext(request))

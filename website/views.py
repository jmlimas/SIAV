#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt                                          
from website.forms import FormaContacto
from django.core.mail import send_mail
from django.db import connections
import requests
import sqlite3
import re
from django.conf import settings
# Create your views here.

def index(request):
    return render_to_response('ericka/index.html', {}, context_instance=RequestContext(request))
@csrf_exempt
def index2(request):  
	forma = FormaContacto()
	class Post:
	   def __init__(self, titulo, slug,contenido,autor,avatar,fecha):
			self.titulo = titulo
			self.slug = slug
			self.contenido = contenido
			self.autor = autor
			self.avatar = avatar
			self.fecha = fecha
		
	   def displayPost(self):
	      print "Name : ", self.titulo,  ", Salary: ", self.fecha
	conn = sqlite3.connect('/var/www/ghost/content/data/ghost.db')
	lista_post = []



	
	#cursor = connections['sqlite'].cursor()
	#cursor.execute('SELECT count(*) FROM posts')

	#row = cursor.fetchone()
	#print row


	cursor = connections['sqlite'].cursor()
	for row in cursor.execute('SELECT t1.title,t1.slug,t1.html,t2.name,t2.image,DATE(t1.created_at) FROM posts t1 LEFT JOIN users t2 on t2.id = t1.published_by WHERE status = "published" ORDER BY published_at'):
		info = (row[2][:200] + '...') if len(row[2]) > 75 else row[2]
		post = Post(row[0],row[1],re.sub('<[^<]+?>', '', info),row[3],row[4],row[5])
		lista_post.append(post)
	mine = row[5]
	return render_to_response('ericka/index2.html',locals(), context_instance=RequestContext(request))

def servicios(request):
    return render_to_response('ericka/services.html', {}, context_instance=RequestContext(request))

def faq(request):
    return render_to_response('ericka/faq.html', {}, context_instance=RequestContext(request))

@csrf_exempt
def contacto(request):
	if request.method == 'POST':
	    # La forma ligada a los datos enviados en el POST
	    forma = FormaContacto(request.POST)
	    # Todas las reglas de validacion aprobadas
	    if forma.is_valid():

	    	if forma.cleaned_data['Captcha'] != '6':
	    		return HttpResponse('Parece que hubo un error en el captcha, intenta de nuevo.')

	    	#send_mail('Contacto Alluxi',forma.cleaned_data['Mensaje'],['gusreyes01@gmail.com',], fail_silently=False)
	        #send_mail('Contacto Alluxi', forma.cleaned_data['Mensaje'], 'hola@gmail.com', ['gusreyes01@gmail.com'], fail_silently=False)

	        r1 = requests.post(
	        "https://api.mailgun.net/v2/alluxi.mx/messages",
	        auth=("api", "key-9snzu8gopo2vt5zdlay-e6ggboizrf27"),
	        data={"from": "Cliente de Alluxi <gustavo@alluxi.mx>",
	              "to": ["gusreyes01@gmail.com"],
	              "subject": forma.cleaned_data['Nombre']+" <"+forma.cleaned_data['Correo']+">, ("+forma.cleaned_data['Telefono']+")",
	              "text": forma.cleaned_data['Mensaje']})
	        return HttpResponse('¡Gracias por tu mensaje! Pronto nos comunicaremos contigo.')  # Redirect after POST
	    else:
			return HttpResponse('Parece que hubo un error. Prueba llenando todos los campos.')
	else:
		forma = FormaContacto()  # An unbound form
		return render_to_response('ericka/index2.html', {'forma':forma}, context_instance=RequestContext(request))









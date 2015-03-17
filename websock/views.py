# -*- encoding: utf-8 -*-
from websock.models import Comments, User, Eventos, Comments, EventoUsuario
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder
import json
import redis
import json as simplejson
from socketIO_client import SocketIO, LoggingNamespace
import urllib2


def socketio_emit(data):
    # message = urllib2.urlopen("http://127.0.0.1:4000").getcode()
    #Verfica que el servidor este arriba
    # if message == 200:
    #     socketIO = SocketIO('127.0.0.1', 4000, params={'q': 'qqq'},headers={'Authorization': 'Basic '},cookies={'a': 'aaa'})
    #     if socketIO:
    #         socketIO.emit('message2',data)
    #         # socketIO.wait(seconds=1)    
    #         socketIO.removeListener('connection', data);

    r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
    r.publish('chat', data)    


@login_required 
def home(request):
    comments = Comments.objects.select_related().all()
    users = User.objects.values_list('first_name','id')
    users_json = json.dumps(list(users), cls=DjangoJSONEncoder)
    return render(request, 'home/chat.html', locals())
 
#   Enviar notificación de evento a usuarios 
@csrf_exempt
def lanza_notif(tipo,avaluo,user):
   
    # r = redis.StrictRedis(host='localhost', port=6379, db=0)

    if tipo == 'VISITA':
        accion = (' visitó el avalúo con FolioK: ').decode("UTF-8", "ignore")
    elif tipo == 'CAPTURA':
        accion = (' capturó el avalúo con FolioK: ').decode("UTF-8", "ignore")
    elif tipo == 'SALUDA':
        accion = (' dió salida al avalúo con FolioK: ').decode("UTF-8", "ignore")
    elif tipo == 'CONSULTA_SENCILLA':
        accion = (' consultó el avalúo con FolioK: ').decode("UTF-8", "ignore")
    elif tipo == 'CONSULTA_MASTER':
        accion = (' editó el avalúo con FolioK: ').decode("UTF-8", "ignore")
    else:
        accion = 'NULL'

    msg = {}
    msg['send_user_id'] = user.id
    #msg['rec_user_id'] = user_to.id  # This events are for all users
    msg['message'] = (user.username + accion + '<b>' + avaluo.FolioK + '</b>')
    data = simplejson.dumps(msg)

    #Publica en Redis para generar notificación
    # r.publish('chat', data)

    socketio_emit(data)


    #Crear evento en BD
    Eventos.objects.create(user=user, evento=tipo, avaluo=avaluo)

#Enviar notificación de chat a usuarios
@csrf_exempt
def node_api(request):
    try:
        #Used ONLY for chat messages, Events are managed in every action on myviews.py
        #Get User from sessionid
        session = Session.objects.get(session_key=request.POST.get('sessionid'))
        user_id = session.get_decoded().get('_auth_user_id')
        message = text=request.POST.get('comment')
        user = User.objects.get(id=user_id)
        user_to = User.objects.get(id=request.POST.get('UserToId'))
 
        msg = {}
        msg['send_user_id'] = user.id
        msg['rec_user_id'] = user_to.id
        msg['message'] = message
        data = simplejson.dumps(msg)


        #Create comment
        Comments.objects.create(user=user, text=data)
        
        #Once comment has been created post it to the chat channel
        #r = redis.StrictRedis(host='localhost', port=6379, db=0)
        #r.publish('chat', data)

        socketio_emit(data)
        
        return HttpResponse("Everything worked :)")
    except Exception, e:
        return HttpResponseServerError(str(e))

def get_notificaciones(request,template='home/consultas/notificaciones.html'):
    comments_enviar = EventoUsuario.objects.filter(recibe_id=request.user).order_by('-date')[:40]
    comments = EventoUsuario.objects.filter(recibe_id=request.user,leido=False).order_by('-date')
    response = render(request,template, locals())
    comments.update(leido=True)
    return response

def get_tolerancia(request,template='home/consultas/tolerancia.html'):
    from django.db import connection, transaction
    cursor = connection.cursor()
    cursor.execute('SELECT t1.avaluo_id, IFNULL(t3.Cliente, "TOTAL") AS name, COUNT(*), SUM(IF(DATEDIFF(CURDATE(),DATE_ADD(t1.Solicitud,INTERVAL t2.tolerancia DAY)) <= 0,1, 0)) as "= 0", SUM(IF(DATEDIFF(CURDATE(),DATE_ADD(t1.Solicitud,INTERVAL t2.tolerancia DAY)) BETWEEN 1 AND 3,1, 0) )as "< 3", SUM(IF(DATEDIFF(CURDATE(),DATE_ADD(t1.Solicitud,INTERVAL t2.tolerancia DAY)) > 3,1, 0)) as "> 3" FROM siavdb.app_avaluo t1 LEFT JOIN siavdb.app_depto t2 on t1.Depto_id = t2.Depto_id LEFT JOIN siavdb.app_cliente t3 on t2.Cliente_id_id = t3.Cliente_id WHERE t1.Estatus in ("PROCESO","DETENIDO") AND (FACTURA IS NULL OR FACTURA = "")  AND (SALIDA IS NULL ) GROUP BY t3.Cliente WITH ROLLUP;')

    en_tiempo = cursor.fetchall()
    cursor.execute('SELECT *, (SELECT COUNT(*) FROM APP_AVALUO X1 WHERE T1.CLIENTE_ID = X1.CLIENTE_ID AND ESTATUS IN ("PROCESO","DETENIDO") AND SALIDA IS NULL AND VISITA IS NULL AND MTERRENO IS NULL AND MCONSTRUCCION IS NULL AND SOLICITUD IS NOT NULL) AS "Visita" ,(SELECT COUNT(*) FROM APP_AVALUO X1 WHERE T1.CLIENTE_ID = X1.CLIENTE_ID AND ESTATUS IN ("PROCESO","DETENIDO") AND SALIDA IS NULL AND VISITA IS NOT NULL AND MTERRENO IS NULL AND MCONSTRUCCION IS NULL AND SOLICITUD IS NOT NULL) AS "Captura" ,(SELECT COUNT(*) FROM APP_AVALUO X1 WHERE T1.CLIENTE_ID = X1.CLIENTE_ID AND ESTATUS IN ("PROCESO","DETENIDO") AND SALIDA IS NULL AND VISITA IS NOT NULL AND MTERRENO IS NOT NULL AND MCONSTRUCCION IS NOT NULL AND SOLICITUD IS NOT NULL) AS "Salida" FROM APP_CLIENTE T1 ORDER BY 2')
    en_proceso = cursor.fetchall()

    response = render(request,template, locals())
    return response


def notificaciones_ind(request):
    return render(request, 'home/consultas/notificaciones_ind.html', locals())



def get_conversaciones(request):
    comments = Comments.objects.all()[:200]
    return render(request, 'home/consultas/conversaciones.html', locals())

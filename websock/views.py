from websock.models import Comments, User, Eventos, Comments, EventoUsuario
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required
 
import redis
 
@login_required 
def home(request):
    comments = Comments.objects.select_related().all()
    return render(request, 'home/chat.html', locals())
 
@csrf_exempt
def node_api(request):
    try:
        #Get User from sessionid
        session = Session.objects.get(session_key=request.POST.get('sessionid'))
        user_id = session.get_decoded().get('_auth_user_id')
        user = User.objects.get(id=user_id)
 
        #Create comment
        Comments.objects.create(user=user, text=request.POST.get('comment'))
        
        #Once comment has been created post it to the chat channel
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        r.publish('chat', user.username + ': ' + request.POST.get('comment'))
        
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
    cursor.execute('SELECT t1.avaluo_id, IFNULL(t3.Cliente, "TOTAL") AS name, COUNT(*), SUM(IF(DATEDIFF(CURDATE(),DATE_ADD(t1.Solicitud,INTERVAL t2.tolerancia DAY)) <= 0,1, 0)) as "= 0", SUM(IF(DATEDIFF(CURDATE(),DATE_ADD(t1.Solicitud,INTERVAL t2.tolerancia DAY)) BETWEEN 1 AND 3,1, 0) )as "< 3", SUM(IF(DATEDIFF(CURDATE(),DATE_ADD(t1.Solicitud,INTERVAL t2.tolerancia DAY)) > 3,1, 0)) as "> 3" FROM siavdb.app_avaluo t1 INNER JOIN siavdb.app_depto t2 on t1.Depto_id = t2.Depto_id INNER JOIN siavdb.app_cliente t3 on t2.Cliente_id_id = t3.Cliente_id WHERE t1.Estatus in ("PROCESO") GROUP BY t3.Cliente WITH ROLLUP;')
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

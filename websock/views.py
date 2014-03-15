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

def get_notificaciones(request):
    comments_enviar = EventoUsuario.objects.filter(recibe_id=request.user).order_by('-date')[:8]
    comments = EventoUsuario.objects.filter(recibe_id=request.user,leido=False).order_by('-date')
    response = render(request, 'home/consultas/notificaciones.html', locals())
    comments.update(leido=True)
    return response

def get_conversaciones(request):
    comments = Comments.objects.all()[:200]
    return render(request, 'home/consultas/conversaciones.html', locals())
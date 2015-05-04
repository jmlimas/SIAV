from django.shortcuts import *
from django.contrib.auth.models import User, Group
import json as simplejson
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Sum, Count, Q
from app.models import Avaluo
from websock.models import EventoUsuario, Comments
import functools
import collections
def get_all_users(request):
    users = User.objects.all().exclude(id=request.user.id)
    users_vl = User.objects.values_list('first_name','id')
    users_json = simplejson.dumps(list(users_vl), cls=DjangoJSONEncoder)
    return locals()

def get_chat_messages(request):
    user_comments = {}
    user_comments = Comments.objects.filter(recibe_id=request.user.id) | Comments.objects.filter(envia_id=request.user.id)
    user_comments = user_comments.order_by('date')
    comments_by_user = collections.defaultdict(list)
    for comment in user_comments:
      #Identificamos el chat
      if comment.envia_id != request.user.id:
        comments_by_user[comment.envia.id].append([comment.envia.first_name+" "+comment.envia.last_name,comment.text,comment.date.strftime('%d/%m/%Y'),comment.leido, False])
      else:
        comments_by_user[comment.recibe.id].append([comment.envia.first_name+" "+comment.envia.last_name,comment.text,comment.date.strftime('%d/%m/%Y'),comment.leido, True])

    comments_by_user.default_factory = None
    #user_comments = Comments.objects.filter(reduce(lambda x, y: x | y, [Q(envia=x1) for x1 in users_v2]))
    return locals()

#   Metodo para contar los avaluos en cada seccion.
def cantidades_en_proceso(request):

    #Conteo avaluos de Captura
    avaluos = (Avaluo.objects
               .values('Folio')
               .filter(Q(Estatus__in=['PROCESO','DETENIDO']))
               .filter(Q(Salida__isnull=True))
               .filter(Q(Visita__isnull=False))
               .exclude(Q(Mterreno__isnull=False) & Q(Mconstruccion__isnull=False) & Q(Solicitud__isnull=False)))
    por_capturar = avaluos.count()

    #Conteo avaluos por Visitar
    avaluos = Avaluo.objects.values('Folio').filter(Estatus__in=['PROCESO','DETENIDO'], Visita__isnull=True, Salida__isnull=True)
    por_visitar = avaluos.count()

    #Conteo avaluos por Salida
    avaluos = (Avaluo.objects
               .values('Folio')
               .filter(Q(Estatus__in=['PROCESO','DETENIDO']))
               .filter(Q(Visita__isnull=False))
               .filter(Q(Salida__isnull=True))
               .exclude(Q(Mterreno__isnull=True))
               .exclude(Q(Mconstruccion__isnull=True)))
    por_salida = avaluos.count()

    #Conteo avaluos en proceso
    avaluos = Avaluo.objects.values('Folio').filter(Estatus__in=['PROCESO','DETENIDO'], Salida__isnull=True)
    en_proceso = avaluos.count()

    #Eventos usuario
    conteo_eventos_usuario = EventoUsuario.objects.values('recibe_id').filter(recibe_id=request.user.id,leido=False).count()

    avaluos = []
    return locals()


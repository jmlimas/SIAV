from django.shortcuts import *
from django.contrib.auth.models import User, Group
import json as simplejson
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Sum, Count, Q
from app.models import Avaluo
from websock.models import EventoUsuario

def get_all_users(request):
    users = User.objects.values_list('first_name','id')
    users_json = simplejson.dumps(list(users), cls=DjangoJSONEncoder)
    return {'users_json':users_json}

#   Metodo para contar los avaluos en cada seccion.
def cantidades_en_proceso(request):

    #Conteo avaluos de Captura
    avaluos = (Avaluo.objects
               .values('FolioK')
               .filter(Q(Estatus__in=['PROCESO','DETENIDO']))
               .filter(Q(Salida__isnull=True))
               .filter(Q(Visita__isnull=False))
               .exclude(Q(Mterreno__isnull=False) & Q(Mconstruccion__isnull=False) & Q(Solicitud__isnull=False)))
    por_capturar = avaluos.count()

    #Conteo avaluos por Visitar
    avaluos = Avaluo.objects.values('FolioK').filter(Estatus__in=['PROCESO','DETENIDO'], Visita__isnull=True, Salida__isnull=True)
    por_visitar = avaluos.count()

    #Conteo avaluos por Salida
    avaluos = (Avaluo.objects
               .values('FolioK')
               .filter(Q(Estatus__in=['PROCESO','DETENIDO']))
               .filter(Q(Visita__isnull=False))
               .filter(Q(Salida__isnull=True))
               .exclude(Q(Mterreno__isnull=True))
               .exclude(Q(Mconstruccion__isnull=True)))
    por_salida = avaluos.count()

    #Conteo avaluos en proceso
    avaluos = Avaluo.objects.values('FolioK').filter(Estatus__in=['PROCESO','DETENIDO'], Salida__isnull=True)
    en_proceso = avaluos.count()

    #Eventos usuario
    conteo_eventos_usuario = EventoUsuario.objects.values('recibe_id').filter(recibe_id=request.user.id,leido=False).count()

    avaluos = []
    return locals()

'''
def cantidades_visita(param):
    #Conteo avaluos de Visita
    avaluos = Avaluo.objects.values('FolioK').filter(Estatus__in=['PROCESO','DETENIDO'], Visita__isnull=True, Salida__isnull=True)
    por_visitar = avaluos.count()
    return por_visitar


def cantidades_salida(param):
 	#Conteo avaluos de Salida
    avaluos = (Avaluo.objects
               .values('FolioK')
               .filter(Q(Estatus__in=['PROCESO','DETENIDO']))
               .filter(Q(Visita__isnull=False))
               .filter(Q(Salida__isnull=True))
               .exclude(Q(Mterreno__isnull=True))
               .exclude(Q(Mconstruccion__isnull=True)))
    por_salida = avaluos.count()
    return por_salida


def cantidades_proceso(param):
    #Conteo de avaluos en proceso
    avaluos = Avaluo.objects.values('FolioK').filter(Estatus__in=['PROCESO','DETENIDO'], Salida__isnull=True)
    en_proceso = avaluos.count()
    #pendientes = [por_capturar, por_visitar, por_salida, en_proceso]
    return en_proceso
 '''
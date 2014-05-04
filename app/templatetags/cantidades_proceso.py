from app.models import Avaluo
from websock.models import EventoUsuario
from django import template
from django.db.models import Sum, Count, Q

register = template.Library()

#   Metodo para contar los avaluos en cada seccion.
def cantidades_captura(param):

    #Conteo avaluos de Captura
    avaluos = (Avaluo.objects
               .filter(Q(Estatus__contains='PROCESO') | Q(Estatus__contains='DETENIDO'))
               .filter(Q(Salida__isnull=True))
               .filter(Q(Visita__isnull=False))
               .exclude(Q(Mterreno__isnull=False) & Q(Mconstruccion__isnull=False) & Q(Solicitud__isnull=False)))
    por_capturar = avaluos.count()
    return por_capturar


def cantidades_visita(param):
    #Conteo avaluos de Visita
    avaluos = Avaluo.objects.filter(Estatus__contains='PROCESO', Visita__isnull=True, Salida__isnull=True) | Avaluo.objects.filter(Estatus__contains='DETENIDO', Visita__isnull=True, Salida__isnull=True)
    por_visitar = avaluos.count()
    return por_visitar


def cantidades_salida(param):
 	#Conteo avaluos de Salida
    avaluos = (Avaluo.objects
               .filter(Q(Estatus='PROCESO') | Q(Estatus__contains='DETENIDO'))
               .filter(Q(Visita__isnull=False))
               .filter(Q(Salida__isnull=True)))

    avaluos = (avaluos
               # .exclude(Valor=0.00)
               # .exclude(Q(Valor__isnull=True))
               # .exclude(Q(Referencia__isnull=True))
                .exclude(Q(Mterreno__isnull=True))
               # .exclude(Q(Importe__isnull=True))
                .exclude(Q(Mconstruccion__isnull=True))
                #.exclude(Q(Valor__exact=''))
                )
    por_salida = avaluos.count()
    return por_salida


def cantidades_proceso(param):
    #Conteo de avaluos en proceso
    avaluos = Avaluo.objects.filter(Estatus__contains='PROCESO', Salida__isnull=True) | Avaluo.objects.filter(Estatus__contains='DETENIDO', Salida__isnull=True)
    en_proceso = avaluos.count()
    #pendientes = [por_capturar, por_visitar, por_salida, en_proceso]

    return en_proceso


def conteo_eventos_usuario(param):
    conteo_eventos_usuario = EventoUsuario.objects.filter(recibe_id=param,leido=False).count()
    return conteo_eventos_usuario

register.filter('cantidades_captura', cantidades_captura)
register.filter('cantidades_visita', cantidades_visita)
register.filter('cantidades_salida', cantidades_salida)
register.filter('cantidades_proceso', cantidades_proceso)
register.filter('conteo_eventos_usuario', conteo_eventos_usuario)
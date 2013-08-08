from django import template
from app.models import *
from datetime import datetime, timedelta

register = template.Library()

def elapsed(anio):
	deptos = Depto.objects.all()
	dias_solicitud = 120
	how_many_days = 30
	dias_transcurridos = 0
	dic = {}
	for d in deptos:
		avaluos = Avaluo.objects.filter(Salida__year=anio).filter(Depto=d.depto_id).filter(Salida__gte=datetime.now()-timedelta(days=how_many_days)).filter(Solicitud__gte=datetime.now()-timedelta(days=dias_solicitud))
		cantidad_avaluos = avaluos.count()
		if cantidad_avaluos > 0:
			for a in avaluos:
				if(a.Salida)and(a.Solicitud):
					diferencia = a.Salida - a.Solicitud
					dias_transcurridos += diferencia.days
				else:
					cantidad_avaluos-= 1
			promedio = dias_transcurridos/cantidad_avaluos
			dic[d.Depto] = promedio	
	return dic.iteritems()


register.filter('elapsed', elapsed)
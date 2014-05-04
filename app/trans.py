from app.models import *

def tr_promedio():
	dias_transcurridos = 0
	deptos = Depto.objects.all()
	for d in deptos:
		avaluo = Avaluo.objects.filter(Salida__year=2012).filter(Depto=d.depto_id)
		cantidad_avaluos = avaluo.count()
		if cantidad_avaluos > 0:
			for a in avaluo:
				if(a.Salida)and(a.Solicitud):
					diferencia = a.Salida - a.Solicitud
					if diferencia.days < 7:
						dias_transcurridos += diferencia.days
					
			promedio = dias_transcurridos/cantidad_avaluos
			return promedio

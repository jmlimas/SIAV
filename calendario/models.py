from django.db import models
from app.models import Avaluo

# Create your models here.
class Evento(models.Model):
	evento_id = models.AutoField(primary_key=True)
	Inicio = models.DateField(null=True,blank=True)
	Fin = models.DateField(null=True,blank=True)
	diaEntero = models.NullBooleanField(null=True,blank=True)
	avaluo = models.ForeignKey(Avaluo,null=True,blank=True)
	asigna = models.ForeignKey("auth.User",null=True,blank=True, related_name='%(class)s_asignacion_created')
	visita = models.ForeignKey("auth.User", limit_choices_to={'groups__name': "Visitadores"},null=True,blank=True, related_name='%(class)s_visita_created')
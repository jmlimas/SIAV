from django.db import models
from django.contrib.auth.models import User
from app.models import Avaluo
from websock.models import *
import datetime
from django.utils.timezone import utc



class Comments(models.Model):
	envia = models.ForeignKey(User, related_name="enviaUsuarioCmt")
	recibe = models.ForeignKey(User, related_name="recibeUsuarioCmt")
	text = models.CharField(max_length=255)
	leido = models.BooleanField(null=False)
	date = models.DateTimeField(auto_now_add=True, blank=True)

class Eventos(models.Model):
	user = models.ForeignKey(User)
	evento = models.CharField(max_length=255)
	avaluo = models.ForeignKey(Avaluo)
	date = models.DateTimeField(auto_now_add=datetime.datetime.now(), blank=True)

	def save(self, **kwargs):
		# Place code here, which is excecuted the same
		# time the ``pre_save``-signal would be

		# Call parent's ``save`` function
		super(Eventos, self).save()
		reciente = Eventos.objects.last()
		active_users = User.objects.filter(is_active='True')
		for usuario in active_users:
			eve_usr = EventoUsuario()
			eve_usr.evento_id = reciente.id
			eve_usr.envia = reciente.user
			eve_usr.recibe = usuario
			eve_usr.leido = False
			eve_usr.save()
        # Place code here, which is excecuted the same
        # time the ``post_save``-signal would be

class EventoUsuario(models.Model):
	evento = models.ForeignKey(Eventos)
	envia = models.ForeignKey(User, related_name="enviaUsuario")
	recibe = models.ForeignKey(User, related_name="recibeUsuario")
	leido = models.BooleanField(null=False)
	date = models.DateTimeField(auto_now_add=datetime.datetime.now(), blank=True)


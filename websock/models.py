from django.db import models
from django.contrib.auth.models import User
from app.models import Avaluo
import datetime
from django.utils.timezone import utc



class Comments(models.Model):
    user = models.ForeignKey(User)
    text = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, blank=True)

class Eventos(models.Model):
	user = models.ForeignKey(User)
	evento = models.CharField(max_length=255)
	avaluo = models.ForeignKey(Avaluo)
	date = models.DateTimeField(auto_now_add=datetime.datetime.now(), blank=True)

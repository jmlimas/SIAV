from django.db import models
from django.contrib.auth.models import User
from app.models import *
import os


# Create your models here.
class Ficha_Tecnica(models.Model):
    folio = models.IntegerField(primary_key=True)
    folio_2 = models.IntegerField(null=True,blank=True,default=None)
    municipio = models.ForeignKey(Municipio)
    region =  models.IntegerField(null=True,blank=True)
    colonia = models.CharField(null=True,blank=True, max_length=255)
    lote_tipo = models.CharField(null=True,blank=True, max_length=255)
    valuador = models.ForeignKey(User, null=True)
    LatitudG = models.DecimalField(null=True, max_digits=12, decimal_places=3)
    LatitudM = models.DecimalField(null=True, max_digits=12, decimal_places=3)
    LatitudS = models.DecimalField(null=True, max_digits=12, decimal_places=3)
    LongitudG = models.DecimalField(null=True, max_digits=12, decimal_places=3)
    LongitudM = models.DecimalField(null=True, max_digits=12, decimal_places=3)
    LongitudS = models.DecimalField(null=True, max_digits=12, decimal_places=3)
    limite_norte = models.CharField(null=True,blank=True, max_length=255)
    limite_sur = models.CharField(null=True,blank=True, max_length=255)
    limite_oriente = models.CharField(null=True,blank=True, max_length=255)
    limite_poniente = models.CharField(null=True,blank=True, max_length=255)
######################################################################################
    servicio_1 = models.CharField(null=True,blank=True, max_length=255)
    servicio_2 = models.CharField(null=True,blank=True, max_length=255)
    servicio_3 = models.CharField(null=True,blank=True, max_length=255)
    condicion = models.CharField(null=True,blank=True, max_length=255)
    equipamiento = models.CharField(null=True,blank=True, max_length=255)
    uso_suelo = models.CharField(null=True,blank=True, max_length=255)
    socioeconomico = models.CharField(null=True,blank=True, max_length=255)
    calidad = models.CharField(null=True,blank=True, max_length=255)
    niveles = models.CharField(null=True,blank=True, max_length=255)
    densidad = models.CharField(null=True,blank=True, max_length=255)
    entorno_urbano_1 = models.CharField(null=True,blank=True, max_length=255)
    entorno_urbano_2 = models.CharField(null=True,blank=True, max_length=255)
    riesgo_1 = models.CharField(null=True,blank=True, max_length=255)
    riesgo_2 = models.CharField(null=True,blank=True, max_length=255)
    valor_propuesto = models.CharField(null=True,blank=True,default=None, max_length=255)
    observaciones =  models.CharField(null=True,blank=True,default=None, max_length=255)
    factor = models.DecimalField(null=True,blank=True,default=None, max_digits=12, decimal_places=2)

    def __unicode__(self):
        if self.folio is None:
            return "N/D"
        else:
            return '%s' % self.folio

class Investigacion_Mercado(models.Model):
    investigacion_id = models.AutoField(primary_key=True)
    ficha_id = models.ForeignKey(Ficha_Tecnica)
    calle = models.CharField(null=True, max_length=255)
    colonia = models.CharField(null=True, max_length=255)
    fuente = models.CharField(null=True, max_length=255)
    telefono = models.CharField(null=True, max_length=255)
    uso = models.CharField(null=True, max_length=255)
    m_terreno = models.CharField(null=True, max_length=255)
    m_construccion = models.CharField(null=True, max_length=255)
    oferta = models.DecimalField(null=True, max_digits=12, decimal_places=2)
    unitario_0 = models.DecimalField(null=True, max_digits=12, decimal_places=2)
    unitario = models.DecimalField(null=True, max_digits=12, decimal_places=2)
    factor = models.DecimalField(null=True, max_digits=12, decimal_places=2)

    def __unicode__(self):
        if self.investigacion_id is None:
            return "N/D"
        else:
            return '%s' % self.investigacion_id

class Valores_Unitarios(models.Model):
    valores_id = models.AutoField(primary_key=True)
    ficha_id = models.ForeignKey(Ficha_Tecnica)
    valor_operacion = models.DecimalField(null=True, max_digits=12, decimal_places=2)
    valor_mercado = models.DecimalField(null=True, max_digits=12, decimal_places=2)
    activo = models.CharField(null=True, max_length=255)
    def __unicode__(self):
        if self.valores_id is None:
            return "N/D"
        else:
            return '%s' % self.valores_id

def get_image_path(folder, filename):
    return os.path.join('media/',str(folder), filename)

class ImagenFicha(models.Model):
    imagen_id = models.AutoField(primary_key=True)
    folio = models.CharField(null=True, max_length=255)
    ficha = models.ForeignKey(Ficha_Tecnica)
    imagen = models.ImageField("Imagen Ficha", upload_to=get_image_path, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.folio)

class ArchivoFicha(models.Model):
    archivo_id = models.AutoField(primary_key=True)
    folio = models.CharField(null=True, max_length=255)
    ficha = models.ForeignKey(Ficha_Tecnica)
    file = models.FileField("Archivo Ficha", upload_to=get_image_path, blank = True, null=True)

    def __unicode__(self):
        return unicode(self.folio)

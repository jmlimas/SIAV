from django.db import models
from decimal import Decimal
import os
from PIL import Image
from django.contrib.auth.models import User

#1. Registrar los cambios con migrate.py makemigrations app
#2. Modificar y realizar nueva migracion

def get_image_path(folder, filename):
    return os.path.join('media/',str(folder), filename)

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to=get_image_path, blank=True)
    color = models.CharField(blank=True, max_length=50)
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

# Create your models here.
class Estado(models.Model):
    estado_id = models.AutoField(primary_key=True)
    clave = models.CharField(null=True, max_length=255)
    Nombre = models.CharField(null=False, max_length=255)
    abrev = models.CharField(null=True, max_length=255)
    is_active = models.BooleanField(null=False, default=1)

    def __unicode__(self):
        if self.Nombre is None:
            return "N/D"
        else:
            return self.Nombre


class Municipio(models.Model):
    municipio_id = models.AutoField(primary_key=True)
    estado_id = models.ForeignKey(Estado)
    clave = models.CharField(null=True, max_length=255)
    Nombre = models.CharField(null=False, max_length=255)
    is_active = models.BooleanField(null=False, default=1)

    def __unicode__(self):
        if self.Nombre is None:
            return "N/D"
        else:
            return self.Nombre


class Valuador(models.Model):
    valuador_id = models.AutoField(primary_key=True)
    Nombre = models.CharField(null=True, max_length=255)
    Apellido = models.CharField(null=True, max_length=255)
    Correo = models.CharField(null=True, max_length=255)
    is_active = models.BooleanField(null=False)

    def __unicode__(self):
        if self.Nombre is None:
            return "N/D"
        else:
            return self.Apellido


class Cliente(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    Cliente = models.CharField(null=False, max_length=255)
    is_active = models.BooleanField(null=False, default=1)

    def __unicode__(self):
        if self.Cliente is None:
            return "N/D"
        else:
            return self.Cliente

class Servicio(models.Model):
    servicio_id = models.AutoField(primary_key=True)
    Servicio = models.CharField(null=False, max_length=255)
    is_active = models.BooleanField(null=False, default=1)

    def __unicode__(self):
        if self.Servicio is None:
            return "N/D"
        else:
            return self.Servicio


class Contacto(models.Model):
    contacto_id = models.AutoField(primary_key=True)
    Nombre = models.CharField(null=True, max_length=255)
    Apellido = models.CharField(null=True, max_length=255)
    Correo = models.CharField(null=True, max_length=255)
    Telefono = models.CharField(null=True, max_length=255)
    is_active = models.BooleanField(null=False)

    def __unicode__(self):
        if self.Nombre is None:
            return "N/D"
        else:
            return unicode(self.Nombre) or u''


class Tipo(models.Model):
    tipo_id = models.AutoField(primary_key=True)
    Tipo = models.CharField(null=False, max_length=255)
    is_active = models.BooleanField(null=False, default=1)

    def __unicode__(self):
        if self.Tipo is None:
            return "N/D"
        else:
            return self.Tipo


class Depto(models.Model):
    depto_id = models.AutoField(primary_key=True)
    cliente_id = models.ForeignKey(Cliente)
    is_active = models.BooleanField(null=False)
    Depto = models.CharField(null=False, max_length=255)
    Razon = models.CharField(null=False, max_length=255)
    RFC = models.CharField(null=False, max_length=255)
    Calle = models.CharField(null=False, max_length=255)
    Colonia = models.CharField(null=False, max_length=255)
    CP = models.CharField(null=False, max_length=255)
    Ciudad = models.CharField(null=False, max_length=150)
    Metodo = models.CharField(null=True, max_length=50)
    Digitos = models.CharField(null=True, max_length=15)
    Tolerancia = models.CharField(null=False, max_length=255)
    base = models.DecimalField(null=True, max_digits=15, decimal_places=2)
    factor = models.DecimalField(null=True, max_digits=6, decimal_places=3)

    def __unicode__(self):
        if self.Depto is None:
            return "N/D"
        else:
            return self.Depto


class Avaluo(models.Model):   
    avaluo_id = models.AutoField(primary_key=True)
    Referencia = models.CharField(null=True, max_length=255, unique=True)
    Folio = models.CharField(null=True, max_length=255, unique=True)
    Calle = models.CharField(null=True, max_length=255)
    NumExt = models.CharField(null=True, max_length=255)
    NumInt = models.CharField(null=True, max_length=255)
    Colonia = models.CharField(null=True, max_length=255)
    #Municipio = models.CharField(null=True, max_length=255)
    Municipio = models.ForeignKey(Municipio, null=True)
    #Estado = models.CharField(null=True, max_length=255)
    Estado = models.ForeignKey(Estado, null=True)
    Servicio = models.ForeignKey(Servicio, null=True)
    Tipo = models.ForeignKey(Tipo, null=True)
    Estatus = models.CharField(null=True, max_length=255)
    Prioridad = models.CharField(null=True, max_length=255)
    Cliente = models.ForeignKey(Cliente, null=True)
    Depto = models.ForeignKey(Depto, null=True)
    Valuador = models.ForeignKey(User, null=True,blank=True)
    Contacto = models.ForeignKey(Contacto, null=True,blank=True)
    Solicitud = models.DateField(null=True)
    Lote_Tipo = models.CharField(null=True, max_length=255,blank=True)          
    Valor_Mterreno = models.CharField(null=True, max_length=255,blank=True)   
    Valor_Mconstruccion = models.CharField(null=True, max_length=255,blank=True)            
    Factor_Terreno = models.CharField(null=True, max_length=255,blank=True)         
    Factor_Construccion = models.CharField(null=True, max_length=255,blank=True)            
    Valor_Terreno_Concluido = models.CharField(null=True, max_length=255,blank=True)            
    Valor_Construccion_Concluido = models.CharField(null=True, max_length=255,blank=True)
    Mterreno = models.DecimalField(null=True, max_digits=12, decimal_places=2,blank=True)
    Mconstruccion = models.DecimalField(null=True, max_digits=12, decimal_places=2,blank=True)
    LatitudG = models.DecimalField(null=True, max_digits=12, decimal_places=3)
    LatitudM = models.DecimalField(null=True, max_digits=12, decimal_places=3)
    LatitudS = models.DecimalField(null=True, max_digits=12, decimal_places=3)
    LongitudG = models.DecimalField(null=True, max_digits=12, decimal_places=3)
    LongitudM = models.DecimalField(null=True, max_digits=12, decimal_places=3)
    LongitudS = models.DecimalField(null=True, max_digits=12, decimal_places=3)
    Declat = models.DecimalField(null=True, max_digits=12, decimal_places=5)
    Declon = models.DecimalField(null=True, max_digits=12, decimal_places=5)
    Visita = models.DateField(null=True)
    Valor = models.DecimalField(null=True,blank=True, max_digits=15, decimal_places=2,default=Decimal(0.00))
    Gastos = models.DecimalField(null=True, max_digits=15, decimal_places=2)
    Importe = models.DecimalField(null=True, max_digits=15, decimal_places=2)
    Salida = models.DateField(null=True)
    Factura = models.CharField(null=True, max_length=30)
    Pagado = models.NullBooleanField(null=True)
    Observaciones = models.CharField(null=True, max_length=255)


class Avaluo2(models.Model):
    avaluo_id = models.AutoField(primary_key=True)
    Referencia = models.CharField(null=True, max_length=255)
    Folio = models.CharField(null=True, max_length=255)
    Calle = models.CharField(null=True, max_length=255,blank=True)
    NumExt = models.CharField(null=True, max_length=255,blank=True)
    NumInt = models.CharField(null=True, max_length=255,blank=True)
    Colonia = models.CharField(null=True, max_length=255,blank=True)
    Municipio = models.CharField(null=True, max_length=255,blank=True)
    Estado = models.CharField(null=True, max_length=255,blank=True)
    Servicio = models.CharField(null=True, max_length=255,blank=True)
    Tipo = models.CharField(null=True, max_length=255,blank=True)
    Estatus = models.CharField(null=True, max_length=255,blank=True)
    Prioridad = models.CharField(null=True, max_length=255,blank=True)
    Cliente = models.CharField(null=True, max_length=255,blank=True)
    Depto = models.CharField(null=True, max_length=255,blank=True)
    Valuador = models.CharField(null=True, max_length=255,blank=True)
    Contacto = models.CharField(null=True, max_length=255,blank=True)
    Solicitud = models.CharField(null=True, max_length=255,blank=True)
    Lote_Tipo = models.CharField(null=True, max_length=255,blank=True)
    Valor_Mterreno = models.CharField(null=True, max_length=255,blank=True)
    Valor_Mconstruccion = models.CharField(null=True, max_length=255,blank=True)
    Factor_Terreno =models.CharField(null=True, max_length=255,blank=True)
    Factor_Construccion = models.CharField(null=True, max_length=255,blank=True)
    Valor_Terreno_Concluido = models.CharField(null=True, max_length=255,blank=True)
    Valor_Construccion_Concluido = models.CharField(null=True, max_length=255,blank=True)
    Mconstruccion = models.CharField(null=True, max_length=255,blank=True)
    Mterreno = models.CharField(null=True, max_length=255,blank=True)
    LatitudG = models.CharField(null=True, max_length=255,blank=True)
    LatitudM = models.CharField(null=True, max_length=255,blank=True)
    LatitudS = models.CharField(null=True, max_length=255,blank=True)
    LongitudG = models.CharField(null=True, max_length=255,blank=True)
    LongitudM = models.CharField(null=True, max_length=255,blank=True)
    LongitudS = models.CharField(null=True, max_length=255,blank=True)
    Visita = models.CharField(null=True, max_length=255,blank=True)
    Valor = models.CharField(null=True, max_length=255,blank=True)
    Observaciones = models.CharField(null=True, max_length=255,blank=True)

class ImagenAvaluo(models.Model):
    imagen_id = models.AutoField(primary_key=True)
    Folio = models.CharField(null=True, max_length=255)
    avaluo = models.ForeignKey(Avaluo, related_name='avaluos')
    imagen = models.ImageField("Imagen Avaluo", upload_to=get_image_path, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.Folio)
    def save(self):
        if not self.imagen:
            return            

        super(ImagenAvaluo, self).save()

        imagen = Image.open(self.imagen)
        if (imagen.size[0] > 1024):
            (width, height) = imagen.size     
            size = ( 1024, 768)
            imagen = imagen.resize(size, Image.ANTIALIAS)
        imagen.save(self.imagen.path)   

    @staticmethod
    def last_photo(avaluo_id):
        last_photo = ImagenAvaluo.objects.filter(avaluo_id=avaluo_id)
        if last_photo:
            last_photo_obj = last_photo.latest('imagen_id')
            return last_photo_obj.imagen.url
        else:
            return ''



class ArchivoAvaluo(models.Model):
    archivo_id = models.AutoField(primary_key=True)
    Folio = models.CharField(null=True, max_length=255)
    avaluo = models.ForeignKey(Avaluo)
    file = models.FileField("Archivo Avaluo", upload_to=get_image_path, blank = True, null=True)

    def __unicode__(self):
        return unicode(self.Folio)
    def save(self):
        if not self.imagen:
            return            

        super(ArchivoAvaluo, self).save()

        imagen = Image.open(self.imagen)
        if (imagen.size[0] > 1024):
            (width, height) = imagen.size     
            size = ( 1024, 768)
            imagen = imagen.resize(size, Image.ANTIALIAS)
        imagen.save(self.imagen.path) 



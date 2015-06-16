from django.db import models
from decimal import Decimal
import os
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from django.contrib.auth.models import User
from django.core.signals import request_finished
from app.signals import post_viewed



def get_image_path(folder, filename):
    return os.path.join('media/',str(folder), filename)

def get_exif_data(image):
    """Returns a dictionary from the exif data of an PIL Image item. Also converts the GPS Tags"""
    exif_data = {}
    info = image._getexif()
    if info:
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                gps_data = {}
                for t in value:
                    sub_decoded = GPSTAGS.get(t, t)
                    gps_data[sub_decoded] = value[t]
 
                exif_data[decoded] = gps_data
            else:
                exif_data[decoded] = value
 
    return exif_data
 
def _get_if_exist(data, key):
    if key in data:
        return data[key]
    
    return None
  
def _convert_to_degress(value):
    x = []
    """Helper function to convert the GPS coordinates stored in the EXIF to degress in float format"""
    d0 = value[0][0]
    d1 = value[0][1]
    d = float(d0) / float(d1)
    x.append(d)
 
    m0 = value[1][0]
    m1 = value[1][1]
    m = float(m0) / float(m1)
    x.append(m)
 
    s0 = value[2][0]
    s1 = value[2][1]
    s = float(s0) / float(s1)
    x.append(s)

    return x
    
    #return d + (m / 60.0) + (s / 3600.0)
 
def get_lat_lon(exif_data, folio_k):
    """Returns the latitude and longitude, if available, from the provided exif_data (obtained through get_exif_data above)"""
    lat = None
    lon = None
 
    if "GPSInfo" in exif_data:    
        gps_info = exif_data["GPSInfo"]
 
        gps_latitude = _get_if_exist(gps_info, "GPSLatitude")
        gps_latitude_ref = _get_if_exist(gps_info, 'GPSLatitudeRef')
        gps_longitude = _get_if_exist(gps_info, 'GPSLongitude')
        gps_longitude_ref = _get_if_exist(gps_info, 'GPSLongitudeRef')
 
        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            #print gps_latitude[0][0], gps_latitude[1][0], gps_latitude[2][0]
            #print gps_longitude[0][0], gps_longitude[1][0], gps_longitude[2][0]
            lat = _convert_to_degress(gps_latitude)
            #if gps_latitude_ref != "N":                     
            #   lat = 0 - lat
 
            lon = _convert_to_degress(gps_longitude)
            #if gps_longitude_ref != "E":
            #    lon = 0 - lon
 
    return lat, lon


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, related_name='userprofile')

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
    FolioK = models.CharField(null=True, max_length=255, unique=True)
    Calle = models.CharField(null=True, max_length=255)
    NumExt = models.CharField(null=True, max_length=255)
    NumInt = models.CharField(null=True, max_length=255)
    Colonia = models.CharField(null=True, max_length=255)
    #Municipio = models.CharField(null=True, max_length=255)
    Municipio = models.ForeignKey(Municipio, null=True)
    #Estado = models.CharField(null=True, max_length=255)
    Estado = models.ForeignKey(Estado, null=True)
    Servicio = models.CharField(null=True, max_length=255)
    Tipo = models.ForeignKey(Tipo, null=True)
    Estatus = models.CharField(null=True, max_length=255)
    Prioridad = models.CharField(null=True, max_length=255)
    Cliente = models.ForeignKey(Cliente, null=True)
    Depto = models.ForeignKey(Depto, null=True)
    Valuador = models.ForeignKey(Valuador, null=True)
    Solicitud = models.DateField(null=True)
    Mterreno = models.DecimalField(null=True, max_digits=12, decimal_places=2)
    Mconstruccion = models.DecimalField(null=True, max_digits=12, decimal_places=2)
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

class ImagenAvaluo(models.Model):
    imagen_id = models.AutoField(primary_key=True)
    FolioK = models.CharField(null=True, max_length=255)
    avaluo = models.ForeignKey(Avaluo, related_name='avaluos')
    imagen = models.ImageField("Imagen Avaluo", upload_to=get_image_path, blank=True, null=True)
    LatitudG = models.DecimalField(null=True,blank=True, max_digits=12, decimal_places=3)
    LatitudM = models.DecimalField(null=True,blank=True, max_digits=12, decimal_places=3)
    LatitudS = models.DecimalField(null=True,blank=True, max_digits=12, decimal_places=3)
    LongitudG = models.DecimalField(null=True,blank=True, max_digits=12, decimal_places=3)
    LongitudM = models.DecimalField(null=True,blank=True, max_digits=12, decimal_places=3)
    LongitudS = models.DecimalField(null=True,blank=True, max_digits=12, decimal_places=3)


    def __unicode__(self):
        return unicode(self.FolioK)
    def save(self):
        if not self.imagen:
            return            

        #Abre la imagen grabada y le cambia el tamanio
        imagen = Image.open(self.imagen)

        #Obtenemos datos de la imagen
        exif_data = get_exif_data(imagen)
        if exif_data:
            lat, lon = get_lat_lon(exif_data, self.FolioK)
            if lat and lon:
                #Guarda GPS de la imagen
                self.LatitudG = lat[0]
                self.LatitudM = lat[1]
                self.LatitudS = lat[2]

                self.LongitudG = lon[0]
                self.LongitudM = lon[1]
                self.LongitudS = lon[2]

                #Enviamos la senal para editar coordenadas de avaluo
                post_viewed.send(sender=self.__class__, instance=self, a=lat, b=lon, c=self.FolioK)


        #Graba la imagen al llegar
        super(ImagenAvaluo, self).save()

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
    FolioK = models.CharField(null=True, max_length=255)
    avaluo = models.ForeignKey(Avaluo)
    file = models.FileField("Archivo Avaluo", upload_to=get_image_path, blank = True, null=True)

    def __unicode__(self):
        return unicode(self.FolioK)
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



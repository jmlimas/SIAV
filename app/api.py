# myapp/api.py
from tastypie.resources import ModelResource
from app.models import Avaluo, ImagenAvaluo, Depto
from django.contrib.auth.models import User
from websock.models import Eventos
from tastypie.serializers import Serializer
from tastypie.resources import ALL
from tastypie import fields
from django.db.models import Sum, Count, Q


class UserResource(ModelResource):
    
    class Meta:
        resource_name = 'user'
        queryset = User.objects.all()
        serializer = Serializer(formats=['json', 'jsonp', 'xml', 'yaml', 'html', 'plist'])





class DeptoResource(ModelResource):

    class Meta:
        queryset = Depto.objects.all()
        resource_name = 'depto'
        serializer = Serializer(formats=['json', 'jsonp', 'xml', 'yaml', 'html', 'plist'])
        excludes = ['depto_id', 'is_active', 'Razon', 'RFC', 'Calle', 'Colonia', 'CP', 'Ciudad', 'Metodo', 'Digitos', 'Tolerancia', 'base', 'factor', 'resource_uri']

class ImagenAvaluoResource(ModelResource):
    class Meta:
        queryset = ImagenAvaluo.objects.all()
        resource_name = 'imagen_avaluo'
        serializer = Serializer(formats=['json', 'jsonp', 'xml', 'yaml', 'html', 'plist'])
        excludes = ['resource_uri','imagen_id']
        filtering = { "FolioK": ALL }

class AvaluoResource(ModelResource):
    depto = fields.ToOneField( DeptoResource, 'Depto', full = True )
    imagen_avaluo = fields.ToManyField('app.api.ImagenAvaluoResource', 'avaluos', full=True, null=True)
    class Meta:
        queryset = Avaluo.objects.filter(Estatus__contains='PROCESO', Salida__isnull=True) | Avaluo.objects.filter(Estatus__contains='DETENIDO', Salida__isnull=True)
        resource_name = 'avaluo'
        serializer = Serializer(formats=['json', 'jsonp', 'xml', 'yaml', 'html', 'plist'])
        filtering = { "FolioK": ALL }



class EstadisticoAsignaResource(ModelResource):
    class Meta:
        queryset = Avaluo.objects.all()
        resource_name = 'estadistico_asigna'
        serializer = Serializer(formats=['json', 'jsonp', 'xml', 'yaml', 'html', 'plist'])
        excludes = ['Servicio','Salida','Valor','Solicitud','avaluo_id','Visita','Referencia','Calle','Colonia','NumExt','NumInt','Prioridad','Pagado','LatitudG','LatitudM','LatitudS','LongitudG','LongitudM','LongitudS','Declat','Declon','Estatus','Mterreno','Mconstruccion']

    def dehydrate(self, bundle):
        transaction = Avaluo.objects.extra(select={'month': 'extract( month from Salida)'}).values('month').filter(Salida__year=2013).order_by('month').annotate(dcount=Count('Solicitud'), Total=Sum('Importe')).distinct()
        filtering = { "anio": ALL }
        return transaction

class EventoResource(ModelResource):
    user = fields.ToOneField(UserResource, 'user', full=True, readonly=True, null=True)
    avaluo = fields.ToOneField(AvaluoResource, 'avaluo', full=True, readonly=True, null=True)

    class Meta:
        resource_name = 'evento'
        queryset = Eventos.objects.all().order_by('-date')    
        serializer = Serializer(formats=['json', 'jsonp', 'xml', 'yaml', 'html', 'plist'])
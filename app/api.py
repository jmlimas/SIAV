# myapp/api.py
from tastypie.resources import ModelResource
from app.models import Avaluo, ImagenAvaluo, Depto
from tastypie.serializers import Serializer
from tastypie.resources import ALL
from tastypie import fields
from django.db.models import Q

class DeptoResource(ModelResource):

    class Meta:
        queryset = Depto.objects.all()
        resource_name = 'depto'
        serializer = Serializer(formats=['json', 'jsonp', 'xml', 'yaml', 'html', 'plist'])
        excludes = ['depto_id', 'is_active', 'Razon', 'RFC', 'Calle', 'Colonia', 'CP', 'Ciudad', 'Metodo', 'Digitos', 'Tolerancia', 'base', 'factor', 'resource_uri']

class AvaluoResource(ModelResource):
    depto = fields.ToOneField( DeptoResource, 'Depto', full = True )

    class Meta:
        queryset = Avaluo.objects.all()


        resource_name = 'avaluo'
        serializer = Serializer(formats=['json', 'jsonp', 'xml', 'yaml', 'html', 'plist'])
        filtering = { "FolioK": ALL }


class ProcesoResource(ModelResource):
    depto = fields.ToOneField( DeptoResource, 'Depto', full = True )

    class Meta:
        proceso = Avaluo.objects.filter(Estatus__contains='PROCESO', Salida__isnull=True) | Avaluo.objects.filter(Estatus__contains='DETENIDO', Salida__isnull=True)
        queryset = proceso.order_by('-Solicitud')


        resource_name = 'proceso'
        serializer = Serializer(formats=['json', 'jsonp', 'xml', 'yaml', 'html', 'plist'])
        filtering = { "FolioK": ALL }



class ImagenAvaluoResource(ModelResource):
    class Meta:
        queryset = ImagenAvaluo.objects.all()
        resource_name = 'imagen_avaluo'
        serializer = Serializer(formats=['json', 'jsonp', 'xml', 'yaml', 'html', 'plist'])
        excludes = ['resource_uri','imagen_id']
        filtering = { "FolioK": ALL }
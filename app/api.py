# myapp/api.py
from tastypie.resources import ModelResource
from app.models import Avaluo, ImagenAvaluo, Depto, UserProfile
from calendario.models import Evento
from django.contrib.auth.models import User
from websock.models import Eventos
from tastypie.serializers import Serializer
from tastypie.resources import ALL
from tastypie.authorization import DjangoAuthorization
from tastypie import fields
from django.db.models import Sum, Count, Q
from app.authentication import OAuth20Authentication
from string import upper
from django.http import HttpResponse
from tastypie.exceptions import ImmediateHttpResponse

__author__ = '@danigosa'

class BaseCorsResource(ModelResource):
    """
    Class implementing CORS
    """
    def create_response(self, *args, **kwargs):
        response = super(BaseCorsResource, self).create_response(*args, **kwargs)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = 'Content-Type'
        return response

    def method_check(self, request, allowed=None):
        if allowed is None:
            allowed = []

        request_method = request.method.lower()
        allows = ','.join(map(str.upper, allowed))

        if request_method == 'options':
            response = HttpResponse(allows)
            response['Access-Control-Allow-Origin'] = '*'
            response['Access-Control-Allow-Headers'] = 'Content-Type'
            response['Allow'] = allows
            raise ImmediateHttpResponse(response=response)

        if not request_method in allowed:
            response = http.HttpMethodNotAllowed(allows)
            response['Allow'] = allows
            raise ImmediateHttpResponse(response=response)

        return request_method

#Base Extended Abstract Model
class BaseModelResource(BaseCorsResource, ModelResource):
    """
    Abstract class sample with template data for the models
    """
    class Meta:
        abstract = True
        #excludes = ['creation_time', 'modification_time', 'deleted']
        #authentication = authorization.ApiKeyAuthenticationExtended()
        #authorization = DjangoAuthorization()
        serializer = Serializer(formats=['json'])
        #paginator_class = Paginator
        #cache = SimpleCache()
        list_allowed_methods = ['get', 'post', 'put']
        detail_allowed_methods = ['get', 'post', 'put']

class UserProfileResource(ModelResource):
    user = fields.ToOneField('app.api.UserResource', attribute='user', related_name='profile')
    class Meta:
        queryset = UserProfile.objects.all()
        resource_name = 'userprofile'
        serializer = Serializer(formats=['json', 'jsonp', 'xml', 'yaml', 'html', 'plist'])

class UserResource(ModelResource):
    userprofile = fields.ToOneField('app.api.UserProfileResource', 'userprofile', full=True, null=True)
    class Meta:
        resource_name = 'user'
        queryset = User.objects.all()
        filtering = { "id": ALL }
        serializer = Serializer(formats=['json', 'jsonp', 'xml', 'yaml', 'html', 'plist'])
        list_allowed_methods = ['get', 'post', 'put']
        detail_allowed_methods = ['get', 'post', 'put']        

class DeptoResource(ModelResource):
    class Meta:
        queryset = Depto.objects.all()
        resource_name = 'depto'
        serializer = Serializer(formats=['json', 'jsonp', 'xml', 'yaml', 'html', 'plist'])
        excludes = ['depto_id', 'is_active', 'Razon', 'RFC', 'Calle', 'Colonia', 'CP', 'Ciudad', 'Metodo', 'Digitos', 'Tolerancia', 'base', 'factor', 'resource_uri']
        # authorization = DjangoAuthorization()
        # authentication = OAuth20Authentication()

class ImagenAvaluoResource(ModelResource):
    class Meta:
        queryset = ImagenAvaluo.objects.all()
        resource_name = 'imagen_avaluo'
        serializer = Serializer(formats=['json', 'jsonp', 'xml', 'yaml', 'html', 'plist'])
        excludes = ['resource_uri','imagen_id']
        filtering = { "FolioK": ALL }
        # authorization = DjangoAuthorization()
        # authentication = OAuth20Authentication()

class EventoCalendarioResource(ModelResource):
    class Meta:
        queryset = Evento.objects.all()
        resource_name = 'calendario'
        serializer = Serializer(formats=['json', 'jsonp', 'xml', 'yaml', 'html', 'plist'])
        # authorization = DjangoAuthorization()
        # authentication = OAuth20Authentication()
    def dehydrate(self, bundle):
        av = Avaluo.objects.get(pk=bundle.obj.avaluo_id)
        bundle.data['FolioK'] = av.FolioK
        bundle.data['Colonia'] = av.Colonia
        return bundle

class FacturaResource(ModelResource):
    Total = fields.FloatField(readonly=True)
    Factura = fields.CharField()
    class Meta:
        queryset = (Avaluo.objects
                .filter(Estatus='CONCLUIDO')
               .filter(Q(Factura__isnull=False))
               .filter(Q(Pagado=0) | Q(Pagado__isnull=True))
               .exclude(Q(Factura__exact='')))
        resource_name = 'factura'
        serializer = Serializer(formats=['json', 'jsonp', 'xml', 'yaml', 'html', 'plist'])

    def dehydrate(self, bundle):
        queryset = (Avaluo.objects
                .filter(Estatus='CONCLUIDO')
               .filter(Q(Factura__isnull=False))
               .filter(Q(Pagado=0) | Q(Pagado__isnull=True))
               .exclude(Q(Factura__exact=''))).values('Factura', 'Cliente__Cliente').annotate(Total=Sum('Importe'), Cantidad=Count('Factura'))  
        filtering = { "anio": ALL }
        return queryset


class AvaluoResource(ModelResource):
    depto = fields.ToOneField( DeptoResource, 'Depto', full = True )
    imagen_avaluo = fields.ToManyField('app.api.ImagenAvaluoResource', 'avaluos', full=True, null=True)
    #avaluo_id = fields.FloatField()
    class Meta:
        queryset = Avaluo.objects.filter(Estatus__contains='PROCESO', Salida__isnull=True) | Avaluo.objects.filter(Estatus__contains='DETENIDO', Salida__isnull=True)
        resource_name = 'avaluo'
        serializer = Serializer(formats=['json', 'jsonp', 'xml', 'yaml', 'html', 'plist'])
        filtering = { "FolioK": ALL }
        # authorization = DjangoAuthorization()
        # authentication = OAuth20Authentication()



class EstadisticoAsignaResource(ModelResource):
    class Meta:
        queryset = Avaluo.objects.all()
        resource_name = 'estadistico_asigna'
        serializer = Serializer(formats=['json', 'jsonp', 'xml', 'yaml', 'html', 'plist'])
        excludes = ['Servicio','Salida','Valor','Solicitud','avaluo_id','Visita','Referencia','Calle','Colonia','NumExt','NumInt','Prioridad','Pagado','LatitudG','LatitudM','LatitudS','LongitudG','LongitudM','LongitudS','Declat','Declon','Estatus','Mterreno','Mconstruccion']
        # authorization = DjangoAuthorization()
        # authentication = OAuth20Authentication()

    def dehydrate(self, bundle):
        transaction = Avaluo.objects.extra(select={'month': 'extract( month from Salida)'}).values('month').filter(Salida__year=2015).order_by('month').annotate(dcount=Count('Solicitud'), Total=Sum('Importe')).distinct()
        filtering = { "anio": ALL }
        return transaction

class EventoResource(ModelResource):
    user = fields.ToOneField(UserResource, 'user', full=True, readonly=True, null=True)
    avaluo = fields.ToOneField(AvaluoResource, 'avaluo', full=True, readonly=True, null=True)

    class Meta:
        resource_name = 'evento'
        queryset = Eventos.objects.all().order_by('-date')    
        serializer = Serializer(formats=['json', 'jsonp', 'xml', 'yaml', 'html', 'plist'])
        # authorization = DjangoAuthorization()
        # authentication = OAuth20Authentication()
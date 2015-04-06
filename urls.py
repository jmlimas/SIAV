from django.conf.urls import patterns, url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import login
from django.contrib import admin
from django.conf import settings
from django.conf import settings
from django.conf.urls import include, patterns, url
from django.core.urlresolvers import reverse
from django.utils.functional import curry
from django.views.defaults import *
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from app.api import *
from tastypie.api import Api
from calendario.urls import *

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(AvaluoResource())
v1_api.register(DeptoResource())
v1_api.register(ImagenAvaluoResource())
v1_api.register(EstadisticoAsignaResource())
v1_api.register(EventoResource())
    # Examples:
    # url(r'^$', 'SIAV.views.home', name='home'),
    #url(r'^SIAV/', include('SIAV.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    # Upload files Urls

urlpatterns = patterns(


    '', url(r'^SIAV/ajax_upload/(\w*\d+)/(\@*\w*\d+)/$', 'app.uploads.ajax_upload', name="ajax_upload"),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^api/', include(v1_api.urls)),
    url(r'^SIAV/admin/', include(admin.site.urls)),



    #Urls del SIAV

    url(r'^SIAV/$', 'app.views.home', name='home'),
    url(r'^SIAV/login/$',  login),
    url(r'^SIAV/logout/', 'app.views.logout_view', name='logout_view'),
    url(r'^SIAV/home/', 'app.views.home', name='home'),


    url(r'^SIAV/cambia_estatus/(?P<match>.+)/$', 'app.views.cambia_estatus', name='cambia_estatus'),

    #url(r'^$', 'app.views.lista_avaluo', name = 'lista_avaluo'),
    url(r'^SIAV/guarda_master/?(\d+)/?$', 'app.views.guarda_master', name='guarda_master'),
    url(r'^SIAV/consulta_master/', 'app.views.consulta_master', name='consulta_master'),
    url(r'^SIAV/consulta_master/(?P<query>)/?$', 'app.views.consulta_master', name='consulta_master'),

    #Consulta de comparables
    url(r'^SIAV/consulta_comparable/', 'app.views.consulta_comparable', name='consulta_comparable'),
    url(r'^SIAV/consulta_comparable/(?P<query>)/?$', 'app.views.consulta_comparable', name='consulta_comparable'),


    #url(r'^SIAV/consulta_sencilla/', 'app.views.consulta_sencilla', name='consulta_sencilla'),
    url(r'^SIAV/respuesta_consulta_sencilla/?(\d+)/?$', 'app.views.respuesta_consulta_sencilla', name='respuesta_consulta_sencilla'),

    url(r'^SIAV/alta_avaluo/', 'app.views.alta_avaluo', name='alta_avaluo'),
    url(r'^SIAV/alta_avaluo_paquete/', 'app.views.alta_avaluo_paquete', name='alta_avaluo_paquete'),
    url(r'^SIAV/actualiza_avaluo/(\d+)/$', 'app.views.actualiza_avaluo', name='actualiza_avaluo'),

    url(r'^SIAV/visita/', 'app.views.visita', name='visita'),
    url(r'^SIAV/edita_visita/(\d+)/$', 'app.views.edita_visita', name='edita_visita'),

    #Url para eventos masivos
    url(r'^SIAV/visita_masiva/$', 'app.views.visita_masiva', name='visita_masiva'),
    url(r'^SIAV/captura_masiva/$', 'app.views.captura_masiva', name='captura_masiva'),
    url(r'^SIAV/salida_masiva/$', 'app.views.salida_masiva', name='salida_masiva'),

    url(r'^SIAV/show_visita_pdf/(\d+)/$', 'app.views.show_visita_pdf', name='show_visita_pdf'),
    url(r'^SIAV/show_orden_visita/$', 'app.views.show_orden_visita', name='show_orden_visita'),
    url(r'^SIAV/show_orden_visita/(?P<avaluo_visitado>)/?$', 'app.views.show_orden_visita', name='show_orden_visita'),

    url(r'^SIAV/captura/', 'app.views.captura', name='captura'),

    #Salida
    url(r'^SIAV/salida/', 'app.views.salida', name='salida'),
    url(r'^SIAV/edita_salida/(\d+)/$', 'app.views.edita_salida', name='edita_salida'),
    #url(r'^SIAV/salida_efectiva/(\d+)/$', 'app.views.salida_efectiva', name='salida_efectiva'),

    #Alta Usuario
    url(r'^SIAV/alta_usuario/', 'app.views.alta_usuario', name='alta_usuario'),
    url(r'^SIAV/lista_usuario/', 'app.views.lista_usuario', name='lista_usuario'),

    url(r'^SIAV/lista_valuador/', 'app.views.lista_valuador', name='lista_valuador'),

    url(r'^SIAV/mapas/', 'app.views.mapas', name='mapas'),

    url(r'^SIAV/facturar/', 'app.views.facturar', name='facturar'),

    url(r'^SIAV/liquidar/', 'app.views.liquidar', name='liquidar'),

    url(r'^SIAV/estadistico_anio_js/', 'app.views.estadistico_anio_js', name='estadistico_anio_js'),
    url(r'^SIAV/estadistico/(\d+)/(\d+)/$', 'app.views.estadistico', name='estadistico'),
    url(r'^SIAV/estadistico_cliente_depto/(\d+)/(\d+)/$', 'app.views.estadistico_cliente_depto', name='estadistico_cliente_depto'),
    #url(r'^SIAV/estadistico/', 'app.views.estadistico', name = 'estadistico'),
    url(r'^SIAV/realtime/', 'app.views.realtime', name = 'realtime'),

    #url(r'^SIAV/submitted/', 'app.views.submitted', name='submitted'),

    url(r'^SIAV/test/', 'app.views.test', name='submitted'),

    url(r'^api/get_colonias/', 'app.views.get_colonias', name='get_colonias'),
    url(r'^api/get_municipios/', 'app.views.get_municipios', name='get_municipios'),
    url(r'^api/get_deptos/', 'app.views.get_deptos', name='get_deptos'),
    url(r'^api/get_visitadores/', 'calendario.views.get_visitadores', name='get_visitadores'),

    url(r'^SIAV/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    #url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/img/favicon.ico'}),

    #Url para eliminar imagen
    url(r'^SIAV/elimina_imagen_captura/(\d+)/(\d+)/$', 'app.views.elimina_imagen_captura', name='elimina_imagen_captura'),

    #Urls del sitio web
    url(r'^$', 'website.views.index', name='index'),
    url(r'^faq/', 'website.views.faq', name='faq'),
    url(r'^servicios/', 'website.views.servicios', name='servicios'),
    url(r'^contacto/', 'website.views.contacto', name='contacto'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'media/'}),

    #Urls del sitio movil
    #url(r'^SIAV/mobile/', 'app.views.mobile', name='mobile'),

    url(r'^swf/', 'app.views.swf', name='swf'),
)

    #Urls para sockets
urlpatterns += patterns('',
    url(r'^SIAV/chat/', 'websock.views.home', name='home'),
    url(r'^get_notificaciones/', 'websock.views.get_notificaciones', name='get_notificaciones'),
    url(r'^get_tolerancia/', 'websock.views.get_tolerancia', name='get_tolerancia'),
    url(r'^notificaciones_ind/', 'websock.views.notificaciones_ind', name='notificaciones_ind'),
    url(r'^get_conversaciones/', 'websock.views.get_conversaciones', name='get_conversaciones'),
    #url(r'^marca_leidos/', 'websock.views.marca_leidos', name='marca_leidos'),
    url(r'^node_api$', 'websock.views.node_api', name='node_api'),

    url(r'^monto_inline/', 'app.views.inline.monto_inline', name='monto_inline'),
    url(r'^factura_inline/', 'app.views.inline.factura_inline', name='factura_inline'),
    url(r"^SIAV/calendario/", include("calendario.urls")),

    #Urls de calendario
    #url(include(r'^calendario/',calendario.urls)),
)


# Add the static files pattern to the url.
urlpatterns += staticfiles_urlpatterns() 
# handler404 = 'app.views.errors.not_found_error'

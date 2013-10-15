from django.conf.urls import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import login
from django.contrib import admin
from django.conf import settings

admin.autodiscover()


    # Examples:
    # url(r'^$', 'SIAV.views.home', name='home'),
    #url(r'^SIAV/', include('SIAV.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    # Upload files Urls

urlpatterns = patterns(


    '', url(r'^SIAV/ajax_upload/(\w*\d+)/(\w*\d+)/$', 'app.uploads.ajax_upload', name="ajax_upload"),

    #url(r'^grappelli/', include('grappelli.urls')),

    url(r'^SIAV/admin/', include(admin.site.urls)),




    #Urls del SIAV

    url(r'^SIAV/$', 'app.views.home', name='home'),
    url(r'^SIAV/login/$',  login),
    url(r'^SIAV/logout/', 'app.views.logout_view', name='logout_view'),
    url(r'^SIAV/home/', 'app.views.home', name='home'),

    #url(r'^$', 'app.views.lista_avaluo', name = 'lista_avaluo'),
    url(r'^SIAV/guarda_master/?(\d+)/?$', 'app.views.guarda_master', name='guarda_master'),
    url(r'^SIAV/consulta_master/', 'app.views.consulta_master', name='consulta_master'),
    url(r'^SIAV/consulta_master/(?P<query>)/?$', 'app.views.consulta_master', name='consulta_master'),

    url(r'^SIAV/consulta_sencilla/', 'app.views.consulta_sencilla', name='consulta_sencilla'),
    url(r'^SIAV/respuesta_consulta_sencilla/?(\d+)/?$', 'app.views.respuesta_consulta_sencilla', name='respuesta_consulta_sencilla'),

    url(r'^SIAV/alta_avaluo/', 'app.views.alta_avaluo', name='alta_avaluo'),
    url(r'^SIAV/actualiza_avaluo/(\d+)/$', 'app.views.actualiza_avaluo', name='actualiza_avaluo'),

    url(r'^SIAV/visita/', 'app.views.visita', name='visita'),
    url(r'^SIAV/edita_visita/(\d+)/$', 'app.views.edita_visita', name='edita_visita'),
    url(r'^SIAV/show_visita_pdf/(\d+)/$', 'app.views.show_visita_pdf', name='show_visita_pdf'),

    url(r'^SIAV/captura/', 'app.views.captura', name='captura'),

    #Salida
    url(r'^SIAV/salida/', 'app.views.salida', name='salida'),
    url(r'^SIAV/edita_salida/(\d+)/$', 'app.views.edita_salida', name='edita_salida'),
    url(r'^SIAV/salida_efectiva/(\d+)/$', 'app.views.salida_efectiva', name='salida_efectiva'),

    #Alta Usuario
    url(r'^SIAV/alta_usuario/', 'app.views.alta_usuario', name='alta_usuario'),
    url(r'^SIAV/lista_usuario/', 'app.views.lista_usuario', name='lista_usuario'),

    url(r'^SIAV/alta_valuador/', 'app.views.alta_valuador', name='alta_valuador'),
    url(r'^SIAV/lista_valuador/', 'app.views.lista_valuador', name='lista_valuador'),

    url(r'^SIAV/mapas/', 'app.views.mapas', name='mapas'),

    url(r'^SIAV/facturar/', 'app.views.facturar', name='facturar'),

    url(r'^SIAV/liquidar/', 'app.views.liquidar', name='liquidar'),

    url(r'^SIAV/estadistico/(\d+)/$', 'app.views.estadistico', name='estadistico'),
    #url(r'^SIAV/estadistico/', 'app.views.estadistico', name = 'estadistico'),

    url(r'^SIAV/submitted/', 'app.views.submitted', name='submitted'),

    url(r'^SIAV/test/', 'app.views.test', name='submitted'),

    url(r'^api/get_colonias/', 'app.views.get_colonias', name='get_colonias'),
    url(r'^api/get_municipios/', 'app.views.get_municipios', name='get_municipios'),
    url(r'^api/get_deptos/', 'app.views.get_deptos', name='get_deptos'),

    url(r'^SIAV/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    #url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/img/favicon.ico'}),

    #Url para eliminar imagen
    url(r'^SIAV/elimina_imagen/(\d+)/(\d+)/$', 'app.views.elimina_imagen', name='elimina_imagen'),

    #Urls del sitio web
    url(r'^$', 'website.views.index', name='index'),
    url(r'^faq/', 'website.views.faq', name='faq'),
    url(r'^servicios/', 'website.views.servicios', name='servicios'),
    url(r'^contacto/', 'website.views.contacto', name='contacto'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'media/'})
)

# Add the static files pattern to the url.
urlpatterns += staticfiles_urlpatterns()

urlpatterns += patterns('',
    url("", include('django_socketio.urls')),
)

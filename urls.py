from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import login, logout
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SIAV.views.home', name='home'),
     #url(r'^SIAV/', include('SIAV.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

     # Upload files Urls                  
     url( r'^SIAV/ajax_upload/(\d+)/$', 'app.uploads.ajax_upload', name="ajax_upload" ),
     url( r'^SIAV/upload_page/$', 'app.uploads.upload_page', name="upload_page" ),
                       
     url(r'^SIAV/admin/', include(admin.site.urls)),
     
     url(r'^SIAV/$', 'app.views.home', name = 'home'),
     url(r'^SIAV/login/$',  login),
     url(r'^SIAV/logout/', 'app.views.logout_view', name = 'logout_view'),
     url(r'^SIAV/home/', 'app.views.home', name = 'home'),
     
     #url(r'^$', 'app.views.lista_avaluo', name = 'lista_avaluo'),

     url(r'^SIAV/consulta_master/?(\d+)/?$', 'app.views.consulta_master', name = 'consulta_master2'),
     url(r'^SIAV/consulta_master/', 'app.views.consulta_master', name = 'consulta_master'),
     

     url(r'^SIAV/alta_avaluo/', 'app.views.alta_avaluo', name = 'alta_avaluo'),
     url(r'^SIAV/actualiza_avaluo/(\d+)/$','app.views.actualiza_avaluo', name = 'actualiza_avaluo'),
	 
     url(r'^SIAV/visita/', 'app.views.visita', name = 'visita'),
     url(r'^SIAV/edita_visita/(\d+)/$','app.views.edita_visita', name = 'edita_visita'),
     url(r'^SIAV/show_visita_pdf/(\d+)/$','app.views.show_visita_pdf', name = 'show_visita_pdf'),
	 
     url(r'^SIAV/captura/', 'app.views.captura', name = 'captura'),
	 
     url(r'^SIAV/salida/', 'app.views.salida', name = 'salida'),
     url(r'^SIAV/edita_salida/(\d+)/$','app.views.edita_salida', name = 'edita_salida'),
     
     url(r'^SIAV/alta_usuario/', 'app.views.alta_usuario', name = 'alta_usuario'),
     url(r'^SIAV/lista_usuario/', 'app.views.lista_usuario', name = 'lista_usuario'),
     
     url(r'^SIAV/alta_valuador/', 'app.views.alta_valuador', name = 'alta_valuador'),
     url(r'^SIAV/lista_valuador/', 'app.views.lista_valuador', name = 'lista_valuador'),
	 
     url(r'^SIAV/mapas/', 'app.views.mapas', name = 'mapas'),
     
     url(r'^SIAV/submitted/', 'app.views.submitted', name = 'submitted'),
                       



)

# Add the static files pattern to the url.
urlpatterns += staticfiles_urlpatterns()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, url, include


urlpatterns = patterns('',
	url(r'^$', 'calendario.views.calendario', name='calendario'),
	url(r'^carga_eventos/$', 'calendario.views.cargaEventos', name="cargaEventos"),
	)
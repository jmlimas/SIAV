from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, url, include

#Urls para app de calendario
urlpatterns = patterns('',
	url(r'^$', 'calendario.views.calendario', name='calendario'),
	url(r'^carga_eventos/$', 'calendario.views.cargaEventos', name="cargaEventos"),
	url(r'^crea_eventos/$', 'calendario.views.creaEventos', name="creaEventos"),
	url(r'^elimina_eventos/$', 'calendario.views.eliminaEventos', name="eliminaEventos"),
	url(r'^actualiza_visitador/$', 'calendario.views.actualizaVisitador', name="actualizaVisitador"),
	)
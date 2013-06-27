from django.contrib import admin
from app.models import *



class adminAvaluo(admin.ModelAdmin):
	list_display = ('FolioK', 'avaluo_id', 'Cliente','Depto','Valor','Solicitud','Visita','Salida','Importe')
	search_fields = ('FolioK', 'avaluo_id','Referencia')

admin.site.register(Avaluo, adminAvaluo)

admin.site.register(Cliente)
admin.site.register(Depto)
admin.site.register(Valuador)
admin.site.register(Municipio)


class adminEstado(admin.ModelAdmin):
	list_display = ('Nombre','clave','abrev',)
	search_fields = ('Nombre',)

admin.site.register(Estado, adminEstado)



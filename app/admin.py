from django.contrib import admin
from app.models import *






class adminAvaluo(admin.ModelAdmin):
	list_display = ('FolioK', 'avaluo_id', 'Cliente','Depto','Valor','Solicitud','Visita','Salida','Importe')
	search_fields = ('FolioK', 'avaluo_id','Referencia')

class adminEstado(admin.ModelAdmin):
	list_display = ('Nombre','clave','abrev',)
	search_fields = ('Nombre',)

class adminCliente(admin.ModelAdmin):
	list_display = ('Cliente',)
	search_fields = ('Cliente',)

class adminDepto(admin.ModelAdmin):
	list_display = ('Depto','cliente_id','is_active','Razon','RFC','Calle','Colonia',)
	search_fields = ('Nombre',)

class adminUserProfile(admin.ModelAdmin):
	list_display = ('user','website','picture','color')
	search_fields = ('user',)



admin.site.register(Avaluo, adminAvaluo)
admin.site.register(Cliente, adminCliente)
admin.site.register(Depto, adminDepto)
admin.site.register(Valuador)
admin.site.register(Municipio)
admin.site.register(Estado, adminEstado)
admin.site.register(UserProfile, adminUserProfile)



from django.db import models
from django import forms

# Create your models here.

class Estado(models.Model):
    estado_id = models.AutoField(primary_key=True)
    clave = models.CharField(null=True, max_length=255)
    Nombre = models.CharField(null=False, max_length=255)
    abrev = models.CharField(null=True, max_length=255)
    is_active = models.BooleanField(null=False,default=1)
    def __unicode__(self):
        if self.Nombre is None:
            return "N/D"
        else:
            return self.Nombre
    
class Municipio(models.Model):
    municipio_id = models.AutoField(primary_key=True)
    estado_id = models.ForeignKey(Estado)
    clave = models.CharField(null=True, max_length=255)
    Nombre = models.CharField(null=False, max_length=255)
    is_active = models.BooleanField(null=False,default=1)

    def __unicode__(self):
        if self.Nombre is None:
            return "N/D"
        else:
            return self.Nombre


class Valuador(models.Model):
    valuador_id = models.AutoField(primary_key=True)
    Nombre = models.CharField(null=True, max_length=255)
    Apellido = models.CharField(null=True, max_length=255)
    Correo = models.CharField(null=True, max_length=255)
    is_active = models.BooleanField(null=False)
    
    def __unicode__(self):
	if self.Nombre is None:
	    return "N/D"
	else:
	    return self.Apellido
		
class Cliente(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    Cliente = models.CharField(null=False, max_length=255)
    
    def __unicode__(self):
	if self.Cliente is None:
	    return "N/D"
	else:
	    return self.Cliente

class Tipo(models.Model):
    tipo_id = models.AutoField(primary_key=True)
    Tipo = models.CharField(null=False, max_length=255)
    
    def __unicode__(self):
	if self.Tipo is None:
	    return "N/D"
	else:
	    return self.Tipo
		
class Depto(models.Model):    
	depto_id = models.AutoField(primary_key=True)
	cliente_id = models.ForeignKey(Cliente)
	is_active = models.BooleanField(null=False)
	Depto = models.CharField(null=False, max_length=255)
	Razon = models.CharField(null=False, max_length=255)
	RFC = models.CharField(null=False, max_length=255)
	Calle = models.CharField(null=False, max_length=255)
	Colonia = models.CharField(null=False, max_length=255)
	CP = models.CharField(null=False, max_length=255)
	Ciudad = models.CharField(null=False, max_length=150)
	Metodo = models.CharField(null=True, max_length=50)
	Digitos = models.CharField(null=True, max_length=15)
	Tolerancia = models.CharField(null=False, max_length=255)
    
        def __unicode__(self):
            if self.Depto is None:
                return "N/D"
            else:
                return self.Depto	
	
class Avaluo(models.Model):
    avaluo_id = models.AutoField(primary_key=True)
    Referencia = models.CharField(null=True, max_length=255)
    FolioK = models.CharField(null=True, max_length=255)
    Calle = models.CharField(null=True, max_length=255)
    NumExt = models.CharField(null=True, max_length=255)
    NumInt = models.CharField(null=True, max_length=255)
    Colonia = models.CharField(null=True, max_length=255)
    #Municipio = models.CharField(null=True, max_length=255)
    Municipio = models.ForeignKey(Municipio, null = True )
    #Estado = models.CharField(null=True, max_length=255)
    Estado = models.ForeignKey(Estado, null = True )
    Servicio = models.CharField(null=True, max_length=255)
    Tipo = models.ForeignKey(Tipo, null = True )
    Estatus = models.CharField(null=True, max_length=255)
    Prioridad = models.CharField(null=True, max_length=255)
    Cliente = models.ForeignKey(Cliente, null = True)
    Depto = models.ForeignKey(Depto, null = True )
    Valuador = models.ForeignKey( Valuador, null = True,)
    Solicitud = models.DateField(null=True)
    Mterreno = models.DecimalField(null=True,max_digits=12, decimal_places=2)
    Mconstruccion = models.DecimalField(null=True,max_digits=12, decimal_places=2)
    LatitudG = models.DecimalField(null=True,max_digits=12, decimal_places=3)
    LatitudM = models.DecimalField(null=True,max_digits=12, decimal_places=3)
    LatitudS = models.DecimalField(null=True,max_digits=12, decimal_places=3)
    LongitudG = models.DecimalField(null=True,max_digits=12, decimal_places=3)
    LongitudM = models.DecimalField(null=True,max_digits=12, decimal_places=3)
    LongitudS = models.DecimalField(null=True,max_digits=12, decimal_places=3)
    Visita = models.DateField(null=True)
    Valor = models.DecimalField(null=True, max_digits=15, decimal_places=2)
    Gastos = models.DecimalField(null=True, max_digits=15, decimal_places=2)
    Importe = models.DecimalField(null=True, max_digits=15, decimal_places=2)
    Salida = models.DateField(null=True)
    Factura = models.CharField(null=True, max_length=30)
    Pagado = models.NullBooleanField(null=True)
    Observaciones = models.CharField(null=True,max_length=255)

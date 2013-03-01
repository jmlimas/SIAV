from app.models import *
from django import forms
from django.forms import ModelForm 
from crispy_forms.helper import FormHelper,reverse
from crispy_forms.layout import *


my_default_errors = {
    'required': 'Se requiere este campo.',
    'invalid': 'Este campo es invalido.'
}

SERVICIOS = (
    ('','N/D'),
    ('AVALUO  CREDITO HIPOTECARIO','AVALUO  CREDITO HIPOTECARIO'),
    ('AVALUO PARA JUICIO','AVALUO PARA JUICIO'),
    ('AVALUO PARA DACION EN PAGO','ESTIMACION POSICIONAMIENTO'),
    ('AVALUO  INFONAVIT PAQUETE','AVALUO  INFONAVIT PAQUETE'),
    ('AVALUO PARA REESTRUCTURA DE CREDITO','AVALUO PARA REESTRUCTURA DE CREDITO'),
    ('AVALUO PARTICULAR','AVALUO PARTICULAR'),
    ('AVALUO PARA COMPRA-VENTA','AVALUO PARA COMPRA-VENTA'),
    ('DICTAMEN TECNICO  PUENTE','DICTAMEN TECNICO  PUENTE'),
    ('INSPECCION DE AVANCE DE OBRA','INSPECCION DE AVANCE DE OBRA'),
    ('AVALUO  INFONAVIT MERCADO ABIERTO','AVALUO INFONAVIT MERCADO ABIERTO'),
    ('ESTIMACION POR POSICIONAMIENTO','ESTIMACION POR POSICIONAMIENTO'),
    ('AVALUO TIPO  PUENTE','AVALUO TIPO  PUENTE'),
    ('DIFERENCIA','DIFERENCIA'),
    ('DICTAMEN TECNICO INFONAVIT','DICTAMEN TECNICO INFONAVIT'),
    ('AVALUO PYME','AVALUO PYME'),
     ('APOYO TECNICO','APOYO TECNICO'),
     ('AVALUO  DE LIQUIDEZ','AVALUO  DE LIQUIDEZ'),
     ('COFINAVIT','COFINAVIT'),
     ('COMPARECER EN JUZGADO','COMPARECER EN JUZGADO'),
     ('AVALUO CREDITO SIMPLE','AVALUO CREDITO SIMPLE'),
     ('AVALUO INFONAVIT RECUPERACION','AVALUO INFONAVIT RECUPERACION'),
     ('FOVISSTE','FOVISSTE'),
     ('INFONAVIT COFINANCIADO','INFONAVIT COFINANCIADO'),    
)


ESTADOS = (
    ('-',''),
    ('NUEVO LEON','NUEVO LEON'),
	('COAHUILA','COAHUILA'),
	('TAMAULIPAS','TAMAULIPAS'),
        ('YUCATAN','YUCATAN'),
)

MUNICIPIOS = (
    ('-',''),
    ('MONTERREY','MONTERREY'),
    ('SAN PEDRO GARZA GARCIA','SAN PEDRO GARZA GARCIA'),
    ('SANTA CATARINA','SANTA CATARINA'),
    ('SANTIAGO','SANTIAGO'),
    ('GUADALUPE','GUADALUPE'),
    ('CADEREYTA','CADEREYTA'),
    ('SALTILLO','SALTILLO'),
    ('REYNOSA','REYNOSA'),
    ('MIGUEL ALEMAN','MIGUEL ALEMAN'),
    ('RIO BRAVO','RIO BRAVO'),
    ('GARCIA','GARCIA'),
    ('APODACA','APODACA'),
    ('SAN FERNANDO','SAN FERNANDO'),
    ('VALLE HERMOSO','VALLE HERMOSO'),
    ('MATAMOROS','MATAMOROS'),
    ('EL CARMEN','EL CARMEN'),
    ('PESQUERIA','PESQUERIA'),
    ('ZUAZUA','ZUAZUA'),
    ('CIENEGA DE FLORES','CIENEGA DE FLORES'),
    ('CD. VICTORIA','CD. VICTORIA'),
    ('SAN NICOLAS','SAN NICOLAS'),
    ('ESCOBEDO','ESCOBEDO'),
    ('LINARES','LINARES'),
    ('MONTEMORELOS','MONTEMORELOS'),

)

ESTATUS = (
    ('PROCESO','PROCESO'),
    ('DETENIDO','DETENIDO'),
    ('CONCLUIDO','CONCLUIDO'),
)

ESTATUSV = (
    ('PROCESO','PROCESO'),
    ('DETENIDO','DETENIDO'),
)

PRIORIDAD = (
        ('3','BAJA'),
        ('2','MEDIA'),
        ('1','ALTA'), 
)

GRUPO = (
    ('-',''),
    ('Admins','Admin'),
    ('Usuarios','Usuario'),
    ('Limitados','Limitados'),
)

MESES = (
    ('01','ENERO'),
    ('02','FEBRERO'),
    ('03','MARZO'),
    ('04','ABRIL'),
    ('05','MAYO'),
    ('06','JUNIO'),
    ('07','JULIO'),
    ('08','AGOSTO'),
    ('09','SEPTIEMBRE'),
    ('10','OCTUBRE'),
    ('11','NOVIEMBRE'),
    ('12','DICIEMBRE'),
)

ANIOS = (
    ('2010','2010'),
    ('2011','2011'),
    ('2012','2012'),
    ('2013','2013'),
    ('2014','2014'),
)


class AltaAvaluo(ModelForm):

    #FolioK = forms.CharField(error_messages=my_default_errors,label="Folio K",required = False)
    Referencia = forms.CharField(error_messages=my_default_errors,required = False)
    Calle = forms.CharField(error_messages=my_default_errors)
    NumExt = forms.CharField(error_messages=my_default_errors,label="Num. Ext.",required = False)
    NumInt = forms.CharField(error_messages=my_default_errors,label="Num. Int.",required = False)
    Colonia = forms.CharField(error_messages=my_default_errors)
    Municipio = forms.ChoiceField(error_messages=my_default_errors,choices=MUNICIPIOS)
    Estado = forms.ChoiceField(error_messages=my_default_errors,choices=ESTADOS)
    Servicio = forms.ChoiceField(error_messages=my_default_errors,choices=SERVICIOS,label="Tipo Servicio")
    #Tipo = forms.ChoiceField(error_messages=my_default_errors,choices=TIPO,label="Tipo Inmueble")
    Estatus = forms.ChoiceField(error_messages=my_default_errors,choices=ESTATUS)
    Prioridad = forms.ChoiceField(error_messages=my_default_errors,choices=PRIORIDAD)
    Solicitud = forms.DateField( label="Fecha Solicitud",widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=['%d/%m/%Y']) 
    Observaciones = forms.CharField(widget=forms.Textarea,required = False)
    Valuador = forms.ModelChoiceField(queryset=Valuador.objects.filter(is_active='True'))


    class Meta:
      model = Avaluo
      exclude = ('avaluo_id','FolioK','LatitudG','LatitudM','LatitudS','LongitudG','LongitudM','LongitudS','Mterreno','Mconstruccion','Visita','Gastos','Importe','Salida','Pagado','Factura',)
        
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-AltaAvaluo'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'alta_avaluo'
        self.helper.layout = Layout(
            Div(
            Div(
                'Alta Avaluo - Entrada',
                'Referencia',
                'Tipo',
                'Calle',
                'NumExt',css_class='span3'),
            Div(
                'NumInt',
                'Colonia',               
                'Municipio',
                'Estado',css_class='span3'),
            Div(
                'Servicio',
                'Estatus',
                'Prioridad',
                'Cliente',css_class='span3'),
            Div(
                'Depto',
                'Valuador',
                'Valor',
                'Solicitud'
                , css_class='span3'),css_class='row-fluid'),
                'Observaciones',
            ButtonHolder(
                Submit('submit', 'Enviar', css_class='btn-success')
            ))
        super(AltaAvaluo, self).__init__(*args, **kwargs)




class VisitaAvaluo(ModelForm):
    Calle = forms.CharField(error_messages=my_default_errors)
    NumExt = forms.CharField(error_messages=my_default_errors,label="Num. Ext.",required = False)
    NumInt = forms.CharField(error_messages=my_default_errors,label="Num. Int.",required = False)
    #Tipo = forms.ChoiceField(error_messages=my_default_errors,choices=TIPO,label="Tipo Inmueble")
    Estatus = forms.ChoiceField(error_messages=my_default_errors,choices=ESTATUSV)
    Visita = forms.DateField( label="Fecha Visita",widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=['%d/%m/%Y']) 
    LatitudG = forms.DecimalField(required = False,label="Lat.Grad.")
    LatitudM = forms.DecimalField(label="Lat.Min.",required = False)
    LatitudS = forms.DecimalField(required = False,label="Lat.Seg.")
    LongitudG = forms.DecimalField(required = False,label="Long.Grad.")
    LongitudM = forms.DecimalField(required = False,label="Long.Min.")
    LongitudS = forms.DecimalField(required = False,label="Long.Seg.")
    Observaciones = forms.CharField(widget=forms.Textarea,required = False)
    
    class Meta:
      model = Avaluo
      exclude = ('avaluo_id','Solicitud','FolioK','Referencia','Prioridad','Colonia','Municipio','Estado','Servicio','Salida','Factura','Cliente','Depto','Valuador','Solicitud','Mterreno','Mconstruccion','Valor','Gastos','Importe','Pagado')

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-VisitaAvaluo'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
            Div(
                'Edita Avaluo - Visita',
                'Calle',
                'NumExt',
                'NumInt',        
                css_class='span3'),
            Div(
                'Visita',
                'Estatus',
                'Tipo'
                ,css_class='span3'),
            Div('LatitudG',
                'LatitudM',
                'LatitudS'
                ,css_class='span3'),
            Div('LongitudG',
                'LongitudM',
                'LongitudS'
                ,css_class='span3'),css_class='row-fluid'),
                'Observaciones',

            ButtonHolder(
                Submit('submit', 'Enviar', css_class='btn-success')
            ))
        super(VisitaAvaluo, self).__init__(*args, **kwargs)

class CapturaAvaluo(ModelForm):
  
    Calle = forms.CharField(error_messages=my_default_errors)
    Calle = forms.CharField(error_messages=my_default_errors,required="True")
    NumExt = forms.CharField(error_messages=my_default_errors,label="Num. Ext.",required = False)
    NumInt = forms.CharField(error_messages=my_default_errors,label="Num. Int.",required = False)
    Colonia = forms.CharField(error_messages=my_default_errors)
    Municipio = forms.CharField(error_messages=my_default_errors)
    Estado = forms.ChoiceField(error_messages=my_default_errors,choices=ESTADOS)
    #Servicio = forms.ChoiceField(error_messages=my_default_errors,choices=SERVICIOS,label="Tipo Servicio")
    #Tipo = forms.ChoiceField(error_messages=my_default_errors,label="Tipo Inmueble")
    Estatus = forms.ChoiceField(error_messages=my_default_errors,choices=ESTATUS)
    Prioridad = forms.ChoiceField(error_messages=my_default_errors,choices=PRIORIDAD)
    Referencia = forms.CharField(error_messages=my_default_errors,required = False)
    Solicitud = forms.DateField( label="Fecha Solicitud",widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=['%d/%m/%Y']) 
    Mterreno = forms.DecimalField(required = False)
    Mconstruccion = forms.DecimalField(required = False)
    LatitudG = forms.DecimalField(required = False,label="Long.Grad.")
    LatitudM = forms.DecimalField(required = False,label="Long.Min.")
    LatitudS = forms.DecimalField(required = False,label="Long.Seg.")
    LongitudG = forms.DecimalField(required = False,label="Lat.Grad.")
    LongitudM = forms.DecimalField(required = False,label="Lat.Min.")
    LongitudS = forms.DecimalField(required = False,label="Lat.Seg.")
    Gastos = forms.DecimalField(required = False)
    Importe = forms.DecimalField(required = False)
    Observaciones = forms.CharField(widget=forms.Textarea,required = False)
    Valuador = forms.ModelChoiceField(queryset=Valuador.objects.filter(is_active='True'))
    
    class Meta:
      model = Avaluo
      exclude = ('Salida','Visita','Pagado','Cliente','Depto','Factura','FolioK')

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-CapturaAvaluo'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
            Div(
                'Edita Avaluo - Captura',
                'Referencia',
                'Calle',
                'NumExt',
                'NumInt',
                'Colonia',
                'Municipio',
                css_class='span3'),
            Div(
                'Estado',
                'Servicio',
                'Tipo',
                'Estatus',
                'Prioridad',
                'Valuador'
                ,css_class='span3'),
            Div('LatitudG',
                'LatitudM',
                'LatitudS',
                'LongitudG',
                'LongitudM',
                'LongitudS'
                ,css_class='span3'),
            Div('Solicitud',
                'Mterreno',
                'Mconstruccion',
                'Valor',
                'Gastos',
                'Importe'
                ,css_class='span3'),css_class='row-fluid'),
                'Observaciones',

            ButtonHolder(
                Submit('submit', 'Enviar', css_class='btn-success')
            ))
        super(CapturaAvaluo, self).__init__(*args, **kwargs)    

class SalidaAvaluo(ModelForm):
    Referencia = forms.CharField(error_messages=my_default_errors,required = True)
    Mterreno = forms.DecimalField(error_messages=my_default_errors,required = True)
    Mconstruccion = forms.DecimalField(error_messages=my_default_errors,required = True)
    Observaciones = forms.CharField(error_messages=my_default_errors,widget=forms.Textarea,required = False)
    Salida = forms.DateField(error_messages=my_default_errors,label="Fecha Salida",widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=['%d/%m/%Y']) 
    Importe = forms.DecimalField(required = True)

    class Meta:
      model = Avaluo
      #exclude = ('Salida','Visita','Pagado','Cliente','Depto','Factura','FolioK')
      fields = ('Mterreno','Mconstruccion','Observaciones','Salida','Importe','Referencia') 

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-SalidaAvaluo'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
            Div(
                'Edita Avaluo - Salida',
                'Referencia',
                'Salida',
                css_class='span3'),
            Div('Solicitud',
                'Mterreno',
                'Mconstruccion',
                css_class='span3'),
            Div('Importe',
                css_class='span3'),css_class='row-fluid'),
                'Observaciones',
            ButtonHolder(
                Submit('submit', 'Enviar', css_class='btn-success')
            ))
        super(SalidaAvaluo, self).__init__(*args, **kwargs)  
        
        
class FormaConsultaMaster(ModelForm):
  
    FolioK = forms.CharField(error_messages=my_default_errors,required = False)
    Calle = forms.CharField(error_messages=my_default_errors,required = False)
    NumExt = forms.CharField(error_messages=my_default_errors,label="Num. Ext.",required = False)
    NumInt = forms.CharField(error_messages=my_default_errors,label="Num. Int.",required = False)
    Colonia = forms.CharField(error_messages=my_default_errors,required = False)
    Municipio = forms.CharField(error_messages=my_default_errors,required = False)
    Estado = forms.CharField(error_messages=my_default_errors,required = False)
    Servicio = forms.CharField(error_messages=my_default_errors,required = False,label="Tipo.Servicio")
    Tipo = forms.ModelChoiceField(required=False, queryset=Tipo.objects.all())
    Estatus = forms.ChoiceField(error_messages=my_default_errors,choices=ESTATUS,required = False)
    Valuador = forms.ModelChoiceField(required=False, queryset=Valuador.objects.all())
    Prioridad = forms.ChoiceField(error_messages=my_default_errors,choices=PRIORIDAD,required = False)
    Referencia = forms.CharField(error_messages=my_default_errors,required = False)
    Solicitud = forms.DateField( label="Fecha Solicitud",widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=['%d/%m/%Y'],required = False) 
    Visita = forms.DateField( label="Fecha Visita",widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=['%d/%m/%Y'],required = False) 
    Mterreno = forms.DecimalField(required = False)
    Mconstruccion = forms.DecimalField(required = False)
    LatitudG = forms.DecimalField(required = False,label="Lat.Grad.")
    LatitudM = forms.DecimalField(required = False,label="Lat.Min.")
    LatitudS = forms.DecimalField(required = False,label="Lat.Seg.")
    LongitudG = forms.DecimalField(required = False,label="Long.Grad.")
    LongitudM = forms.DecimalField(required = False,label="Long.Min.")
    LongitudS = forms.DecimalField(required = False,label="Long.Seg.")
    Valor = forms.DecimalField(required = False)
    Gastos = forms.DecimalField(required = False)
    Importe = forms.DecimalField(required = False)
    Observaciones = forms.CharField(widget=forms.Textarea,required = False)
    Mes = forms.ChoiceField(error_messages=my_default_errors,choices=MESES,required=False)
    Anio = forms.ChoiceField(error_messages=my_default_errors,choices=ANIOS,required=False)
  
    class Meta:
      model = Avaluo
      exclude = ('Salida','Pagado','Cliente','Depto','Factura','Prioridad')

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-FormaConsultaMaster'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
            Div(Fieldset
                ('Fecha:',
                'Mes',
                'Anio'),
                css_class='span3'),
            Div(
                'Edita Avaluo - Captura',
                'FolioK',
                'Referencia',
                'Calle',
                'NumExt',
                'NumInt',
                css_class='span3'),
            Div(
                'Colonia',
                'Municipio',
                'Estado',
                'Servicio',
                'Tipo',
                css_class='span3'),css_class='row-fluid'),
            ButtonHolder(
                Submit('Buscar', 'Buscar', css_class='button white'),
                #Submit('Guardar', 'Guardar', css_class='btn-success')
            ))
        super(FormaConsultaMaster, self).__init__(*args, **kwargs)         
        
        
class RespuestaConsultaMaster(ModelForm):
  
    FolioK = forms.CharField(error_messages=my_default_errors,required = False)
    Calle = forms.CharField(error_messages=my_default_errors,required = False)
    NumExt = forms.CharField(error_messages=my_default_errors,label="Num. Ext.",required = False)
    NumInt = forms.CharField(error_messages=my_default_errors,label="Num. Int.",required = False)
    Colonia = forms.CharField(error_messages=my_default_errors,required = False)
    Municipio = forms.CharField(error_messages=my_default_errors,required = False)
    Estado = forms.ChoiceField(error_messages=my_default_errors,choices=ESTADOS,required = False)
    Servicio = forms.CharField(error_messages=my_default_errors,required = False,label="Tipo.Servicio")
    #Tipo = forms.ModelChoiceField(required=False, queryset=Tipo.objects.all())
    Estatus = forms.ChoiceField(error_messages=my_default_errors,choices=ESTATUS,required = False)
    Valuador = forms.ModelChoiceField(required=False, queryset=Valuador.objects.all())
    Prioridad = forms.ChoiceField(error_messages=my_default_errors,choices=PRIORIDAD,required = False)
    Referencia = forms.CharField(error_messages=my_default_errors,required = False)
    Solicitud = forms.DateField( label="Fecha Solicitud",widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=['%d/%m/%Y'],required = False) 
    Visita = forms.DateField( label="Fecha Visita",widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=['%d/%m/%Y'],required = False) 
    Salida = forms.DateField( label="Fecha Salida",widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=['%d/%m/%Y'],required = False) 
    Mterreno = forms.DecimalField(required = False)
    Mconstruccion = forms.DecimalField(required = False)
    LatitudG = forms.DecimalField(required = False,label="Lat.Grad.")
    LatitudM = forms.DecimalField(required = False,label="Lat.Min.")
    LatitudS = forms.DecimalField(required = False,label="Lat.Seg.")
    LongitudG = forms.DecimalField(required = False,label="Long.Grad.")
    LongitudM = forms.DecimalField(required = False,label="Long.Min.")
    LongitudS = forms.DecimalField(required = False,label="Long.Seg.")
    Valor = forms.DecimalField(required = False)
    Gastos = forms.DecimalField(required = False)
    Importe = forms.DecimalField(required = False)
    Observaciones = forms.CharField(widget=forms.Textarea,required = False)
    Factura = forms.CharField(error_messages=my_default_errors,required = False)
    Pagado = forms.BooleanField(required=False)
    class Meta:
      model = Avaluo
      exclude = ('Cliente','Depto','Prioridad')

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-RespuestaConsultaMaster'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
            Div(
                'Edita Avaluo - Captura',
                'FolioK',
                'Referencia',
                'Calle',
                'NumExt',
                'NumInt',
                'Colonia',
                'Tipo',
                css_class='span3'),
            Div(
                'Municipio',
                'Estado',
                'Servicio',
                'Estatus',
                'Valuador',
                'Visita',
                'Factura'
                ,css_class='span3'),  
            Div(
                'LatitudG',
                'LatitudM',
                'LatitudS',
                'LongitudG',
                'LongitudM',
                'LongitudS',
                'Pagado'
                ,css_class='span3'),
            Div('Salida',
                'Mterreno',
                'Mconstruccion',
                'Valor',
                'Gastos',
                'Solicitud',
                'Importe'
                ,css_class='span3'),css_class='row-fluid'),
                'Observaciones',

            ButtonHolder(
                #Submit('Buscar', 'Buscar', css_class='button white'),
                Submit('Guardar', 'Guardar', css_class='btn-success')
            ))
        super(RespuestaConsultaMaster, self).__init__(*args, **kwargs)      
        
class FormaConsultaSencilla(ModelForm):
  
    FolioK = forms.CharField(error_messages=my_default_errors,required = False)
    Calle = forms.CharField(error_messages=my_default_errors,required = False)
    NumExt = forms.CharField(error_messages=my_default_errors,label="Num. Ext.",required = False)
    NumInt = forms.CharField(error_messages=my_default_errors,label="Num. Int.",required = False)
    Colonia = forms.CharField(error_messages=my_default_errors,required = False)
    Municipio = forms.CharField(error_messages=my_default_errors,required = False)
    Estado = forms.CharField(error_messages=my_default_errors,required = False)
    Servicio = forms.CharField(error_messages=my_default_errors,required = False,label="Tipo.Servicio")
    Tipo = forms.ModelChoiceField(required=False, queryset=Tipo.objects.all())
    Estatus = forms.ChoiceField(error_messages=my_default_errors,choices=ESTATUS,required = False)
    Valuador = forms.ModelChoiceField(required=False, queryset=Valuador.objects.all())
    Prioridad = forms.ChoiceField(error_messages=my_default_errors,choices=PRIORIDAD,required = False)
    Referencia = forms.CharField(error_messages=my_default_errors,required = False)
    Solicitud = forms.DateField( label="Fecha Solicitud",widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=['%d/%m/%Y'],required = False) 
    Visita = forms.DateField( label="Fecha Visita",widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=['%d/%m/%Y'],required = False) 
    Mterreno = forms.DecimalField(required = False)
    Mconstruccion = forms.DecimalField(required = False)
    LatitudG = forms.DecimalField(required = False,label="Lat.Grad.")
    LatitudM = forms.DecimalField(required = False,label="Lat.Min.")
    LatitudS = forms.DecimalField(required = False,label="Lat.Seg.")
    LongitudG = forms.DecimalField(required = False,label="Long.Grad.")
    LongitudM = forms.DecimalField(required = False,label="Long.Min.")
    LongitudS = forms.DecimalField(required = False,label="Long.Seg.")
    Valor = forms.DecimalField(required = False)
    Gastos = forms.DecimalField(required = False)
    Importe = forms.DecimalField(required = False)
    Observaciones = forms.CharField(widget=forms.Textarea,required = False)
    Mes = forms.ChoiceField(error_messages=my_default_errors,choices=MESES,required=False)
    Anio = forms.ChoiceField(error_messages=my_default_errors,choices=ANIOS,required=False)
    class Meta:
      model = Avaluo
      exclude = ('Salida','Pagado','Cliente','Depto','Factura','Prioridad')

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-FormaConsultaSencilla'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        #self.helper.form_action = 'lista_consulta_sencilla'
        self.helper.layout = Layout(
            Div(
            Div(Fieldset
                ('Fecha:',
                 'Mes',
                 'Anio'),
                css_class='span3'),
            Div(
                'Edita Avaluo - Captura',
                'FolioK',
                'Referencia',
                'Calle',
                'NumExt',
                'NumInt',
                css_class='span3'),
            Div(
                'Colonia',
                'Municipio',
                'Estado',
                'Servicio',
                'Tipo',
                css_class='span3'),css_class='row-fluid'),
            ButtonHolder(
                Submit('Buscar', 'Buscar', css_class='btn-success'),
            ))
        super(FormaConsultaSencilla, self).__init__(*args, **kwargs)         
           
          
    
class AltaValuador(ModelForm):
    Nombre = forms.CharField(error_messages=my_default_errors)
    Apellido = forms.CharField(error_messages=my_default_errors)
    Correo = forms.CharField(error_messages=my_default_errors)

    class Meta:
      model = Valuador

class AltaUsuario(forms.Form):
  """ 
  Form for creating new login
  """
  Nombre = forms.CharField(error_messages=my_default_errors)
  Correo = forms.CharField(error_messages=my_default_errors)
  Usuario = forms.CharField(error_messages=my_default_errors)
  Contrasena = forms.CharField(widget=forms.PasswordInput)
  Repetir_Contrasena = forms.CharField(widget=forms.PasswordInput)
  Repetir_Contrasena = forms.CharField(widget=forms.PasswordInput)
  Grupo = forms.ChoiceField(choices=GRUPO)
  
  def clean(self):
    try:
      if self.cleaned_data['Contrasena'] != self.cleaned_data['Repetir_Contrasena']:
        raise forms.ValidationError("Las contrasenas no coinciden.")
    except KeyError:
      # didn't find what we expected in data - fields are blank on front end.  Fields
      # are required by default so we don't need to worry about validation
      pass
    return self.cleaned_data


class FacturaForm(ModelForm):
    Factura = forms.CharField(error_messages=my_default_errors,label="")

    class Meta:
      model = Avaluo
      fields = ('avaluo_id','Factura')

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-FacturaForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'POST'
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(Div('Factura',
                css_class='span3'),css_class='row-fluid'),)
        super(FacturaForm, self).__init__(*args, **kwargs)     



class CobrarForm(ModelForm):
    Pagado = forms.BooleanField(required=False,label="")

    class Meta:
      model = Avaluo
      fields = ('avaluo_id','Pagado')

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-CobrarForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'POST'
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(Div('Pagado',
                css_class='span3'),css_class='row-fluid'),)
        super(CobrarForm, self).__init__(*args, **kwargs)     
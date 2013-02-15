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
    ('APODACA','APODACA'),
    ('SAN FERNANDO','SAN FERNANDO'),
    ('VALLE HERMOSO','VALLE HERMOSO'),
    ('MATAMOROS','MATAMOROS'),
    ('EL CARMEN','EL CARMEN'),
    ('CIENEGA DE FLORES','CIENEGA DE FLORES'),
    ('CD. VICTORIA','CD. VICTORIA'),
    ('SAN NICOLAS','SAN NICOLAS'),
    ('ESCOBEDO','ESCOBEDO'),
    ('LINARES','LINARES'),
    ('MONTEMORELOS','MONTEMORELOS'),
    ('GARCIA','GARCIA'),
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
                Submit('submit', 'Enviar', css_class='button white')
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
                Submit('submit', 'Enviar', css_class='button white')
            ))
        super(VisitaAvaluo, self).__init__(*args, **kwargs)

class CapturaAvaluo(ModelForm):
  
    Calle = forms.CharField(error_messages=my_default_errors)
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
    LatitudG = forms.DecimalField(required = False,label="Lat.Grad.")
    LatitudM = forms.DecimalField(required = False,label="Lat.Min.")
    LatitudS = forms.DecimalField(required = False,label="Lat.Seg.")
    LongitudG = forms.DecimalField(required = False,label="Long.Grad.")
    LongitudM = forms.DecimalField(required = False,label="Long.Min.")
    LongitudS = forms.DecimalField(required = False,label="Long.Seg.")
    Gastos = forms.DecimalField(required = False)
    Importe = forms.DecimalField(required = False)
    Observaciones = forms.CharField(widget=forms.Textarea,required = False)
    
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
                Submit('submit', 'Enviar', css_class='button white')
            ))
        super(CapturaAvaluo, self).__init__(*args, **kwargs)    

class SalidaAvaluo(ModelForm):
    Mterreno = forms.DecimalField(error_messages=my_default_errors,required = True)
    Mconstruccion = forms.DecimalField(error_messages=my_default_errors,required = True)
    Observaciones = forms.CharField(error_messages=my_default_errors,widget=forms.Textarea,required = False)
    Salida = forms.DateField(error_messages=my_default_errors,label="Fecha Salida",widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=['%d/%m/%Y']) 

    class Meta:
      model = Avaluo
      #exclude = ('Salida','Visita','Pagado','Cliente','Depto','Factura','FolioK')
      fields = ('Mterreno','Mconstruccion','Observaciones','Salida') 

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-SalidaAvaluo'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
            Div(
                'Edita Avaluo - Salida',
                'Salida',
                css_class='span3'),
            Div('Solicitud',
                'Mterreno',
                'Mconstruccion',
                css_class='span3'),css_class='row-fluid'),
                'Observaciones',

            ButtonHolder(
                Submit('submit', 'Enviar', css_class='button white')
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
    Inicial = forms.DateField(error_messages=my_default_errors,widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=['%d/%m/%Y'],required = False)
    Final = forms.DateField(error_messages=my_default_errors, widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=['%d/%m/%Y'],required = False)
    
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
            Div(
                'Edita Avaluo - Captura',
                'FolioK',
                'Referencia',
                'Calle',
                'NumExt',
                'NumInt',
                'Colonia',

                css_class='span3'),
            Div(
                'Municipio',
                'Estado',
                'Servicio',
                'Tipo',
                css_class='span3'),
                """
                'Servicio',
                'Tipo',
                'Estatus',
                'Valuador'
                ,css_class='span3'),
            Div(
                'LatitudG',
                'LatitudM',
                'LatitudS',
                'LongitudG',
                'LongitudM',
                'LongitudS'
                ,css_class='span3'),
            """,
            Div(Fieldset
                ('Fechas',
                 'Inicial',
                'Final'),
                #'Mterreno',
                #'Mconstruccion',
                #'Valor',
                #'Gastos',
                #'Visita',
                #'Importe'
                css_class='span3'),css_class='row-fluid'),
                #'Observaciones',

            ButtonHolder(
                Submit('Buscar', 'Buscar', css_class='button white'),
                Submit('Guardar', 'Guardar', css_class='button white')
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
    Servicio = forms.ChoiceField(error_messages=my_default_errors,choices=SERVICIOS,label="Tipo Servicio",required = False)
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
    
    class Meta:
      model = Avaluo
      exclude = ('Salida','Pagado','Cliente','Depto','Factura','Prioridad')

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

                css_class='span3'),
            Div(
                'Municipio',
                'Estado',
                'Servicio',
                'Tipo',
                'Estatus',
                'Valuador'
                ,css_class='span3'),  
            Div(
                'LatitudG',
                'LatitudM',
                'LatitudS',
                'LongitudG',
                'LongitudM',
                'LongitudS',css_class='span3'),
            Div('Solicitud',
                'Mterreno',
                'Mconstruccion',
                'Valor',
                'Gastos',
                'Visita',
                'Importe'
                ,css_class='span3'),css_class='row-fluid'),
                'Observaciones',

            ButtonHolder(
                Submit('Buscar', 'Buscar', css_class='button white'),
                Submit('Guardar', 'Guardar', css_class='button white')
            ))
        super(RespuestaConsultaMaster, self).__init__(*args, **kwargs)         
          
    
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
      
      

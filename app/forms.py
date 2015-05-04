# -*- encoding: utf-8 -*-
import datetime
from app.models import *
from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper, reverse
from crispy_forms.layout import *
from django.forms import fields, models, formsets, widgets


SERVICIOS = (
    ('', 'N/D'),
    ('AVALUO  CREDITO HIPOTECARIO', 'AVALUO  CREDITO HIPOTECARIO'),
    ('AVALUO PARA JUICIO', 'AVALUO PARA JUICIO'),
    ('AVALUO PARA DACION EN PAGO', 'ESTIMACION POSICIONAMIENTO'),
    ('AVALUO  INFONAVIT PAQUETE', 'AVALUO  INFONAVIT PAQUETE'),
    ('AVALUO PARA REESTRUCTURA DE CREDITO', 'AVALUO PARA REESTRUCTURA DE CREDITO'),
    ('AVALUO PARTICULAR', 'AVALUO PARTICULAR'),
    ('DICTAMEN TECNICO  PUENTE', 'DICTAMEN TECNICO  PUENTE'),
    ('INSPECCION DE AVANCE DE OBRA', 'INSPECCION DE AVANCE DE OBRA'),
    ('AVALUO  INFONAVIT MERCADO ABIERTO', 'AVALUO INFONAVIT MERCADO ABIERTO'),
    ('ESTIMACION POR POSICIONAMIENTO', 'ESTIMACION POR POSICIONAMIENTO'),
    ('AVALUO TIPO  PUENTE', 'AVALUO TIPO  PUENTE'),
    ('DIFERENCIA', 'DIFERENCIA'),
    ('DICTAMEN TECNICO INFONAVIT', 'DICTAMEN TECNICO INFONAVIT'),
    ('AVALUO PYME', 'AVALUO PYME'),
    ('APOYO TECNICO', 'APOYO TECNICO'),
    ('AVALUO  DE LIQUIDEZ', 'AVALUO  DE LIQUIDEZ'),
    ('COFINAVIT', 'COFINAVIT'),
    ('COMPARECER EN JUZGADO', 'COMPARECER EN JUZGADO'),
    ('AVALUO CREDITO SIMPLE', 'AVALUO CREDITO SIMPLE'),
    ('AVALUO INFONAVIT RECUPERACION', 'AVALUO INFONAVIT RECUPERACION'),
    ('FOVISSTE', 'FOVISSTE'),
    ('INFONAVIT COFINANCIADO', 'INFONAVIT COFINANCIADO'),
    ('VERIFICACION DE GARANTIA 1480', 'VERIFICACION DE GARANTIA 1480'),
)

ESTATUS = (
    ('PROCESO', 'PROCESO'),
    ('DETENIDO', 'DETENIDO'),
    ('CONCLUIDO', 'CONCLUIDO'),
    ('CANCELADO', 'CANCELADO'),
)

ESTATUSV = (
    ('PROCESO', 'PROCESO'),
    ('DETENIDO', 'DETENIDO'),
    ('CANCELADO', 'CANCELADO'),
)

PRIORIDAD = (
    ('3', 'BAJA'),
    ('2', 'MEDIA'),
    ('1', 'ALTA'),
)

GRUPO = (
    ('-', ''),
    ('Admins', 'Admin'),
    ('Usuarios', 'Usuario'),
    ('Limitados', 'Limitados'),
)

MESES = (
    ('', ''),
    ('01', 'ENERO'),
    ('02', 'FEBRERO'),
    ('03', 'MARZO'),
    ('04', 'ABRIL'),
    ('05', 'MAYO'),
    ('06', 'JUNIO'),
    ('07', 'JULIO'),
    ('08', 'AGOSTO'),
    ('09', 'SEPTIEMBRE'),
    ('10', 'OCTUBRE'),
    ('11', 'NOVIEMBRE'),
    ('12', 'DICIEMBRE'),
)

ANIOS = (
    ('', ''),
    ('2010', '2010'),
    ('2011', '2011'),
    ('2012', '2012'),
    ('2013', '2013'),
    ('2014', '2014'),
)

class UserFullName(User):
    class Meta:
        proxy = True

    def __unicode__(self):
        return self.get_full_name()

class AltaAvaluo(ModelForm):

    Referencia = forms.CharField(required=False, label="Expediente Catastral")
    Calle = forms.CharField()
    NumExt = forms.CharField(label="Num. Ext.", required=False)
    NumInt = forms.CharField(label="Num. Int.", required=False)
    Colonia = forms.CharField()
    Tipo = forms.ModelChoiceField(queryset=Tipo.objects.filter(is_active='True'),label="Tipo de Bien")
    Municipio = forms.ModelChoiceField(queryset=Municipio.objects.filter(estado_id__is_active='True'))
    Estado = forms.ModelChoiceField(queryset=Estado.objects.filter(is_active='True'))
    Servicio = forms.ModelChoiceField(queryset=Servicio.objects.filter(is_active='True'),label="Tipo de Servicio")    
    Estatus = forms.ChoiceField(choices=ESTATUS)
    Prioridad = forms.ChoiceField(choices=PRIORIDAD)
    Depto = forms.ModelChoiceField(queryset=Depto.objects.filter(is_active='True'))
    Solicitud = forms.DateField(label="Fecha Solicitud", widget=forms.DateInput(format='%d/%m/%Y'),  input_formats=['%d/%m/%Y'])
    Lote_Tipo = forms.CharField(required=False)
    LatitudG = forms.DecimalField(required=False, label="Lon.G.")
    LatitudM = forms.DecimalField(required=False, label="Lon.M.",)
    LatitudS = forms.DecimalField(required=False, label="Lon.S.")
    LongitudG = forms.DecimalField(required=False, label="Lat.G.")
    LongitudM = forms.DecimalField(required=False, label="Lat.M.")
    LongitudS = forms.DecimalField(required=False, label="Lat.S.")  
    Observaciones = forms.CharField(widget=forms.Textarea, required=False)
    Valor = forms.DecimalField(required=False, widget=forms.TextInput())
    Valuador = forms.ModelChoiceField(queryset=UserFullName.objects.filter(groups__name='Valuadores'))
    Contacto = forms.ModelChoiceField(queryset=Contacto.objects.filter(is_active='True'),label="Contacto para visita",required=False)

    class Meta:
        model = Avaluo
        exclude = ('avaluo_id','Folio', 
                   'Visita','Gastos', 'Importe', 'Salida', 'Pagado', 'Factura', 'Prioridad','Valor_Construccion_Concluido','Valor_Terreno_Concluido','Factor_Terreno',
                   'Factor_Construccion','Valor_Mterreno','Valor_Mconstruccion','Declat','Declon' )
    def clean_Referencia(self):
        return self.cleaned_data['Referencia'] or None
    def __init__(self,  *args,  **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-AltaAvaluo'
        self.helper.form_class = ''
        self.helper.form_method = 'post'
        self.helper.form_action = 'alta_avaluo'
        self.helper.layout = Layout(
            Div(
                Div(
                    'Alta Avaluo - Entrada',
                    'Referencia',
                    'Tipo',
                    'Calle',
                    'NumExt',
                    'NumInt',
                    'Estatus', css_class='col-md-3'),
                Div(
                    'Lote_Tipo',
                    'Colonia',
                    'Estado',
                    'Municipio',
                    'Contacto',
                    'Prioridad', css_class='col-md-3'),
                Div(
                    Div(
                        Div(Field('LatitudG',  css_class='col-md-20 input-small'),  css_class='col-md-4'),
                        Div(Field('LatitudM',  css_class='col-md-20 input-small'),  css_class='col-md-4'),
                        Div(Field('LatitudS',  css_class='col-md-20 input-small'),  css_class='col-md-4')),
                    Div(
                        Div(Field('LongitudG',  css_class='col-md-20 input-small'),  css_class='col-md-4'),
                        Div(Field('LongitudM',  css_class='col-md-20 input-small'),  css_class='col-md-4'),
                        Div(Field('LongitudS',  css_class='col-md-20 input-small'),  css_class='col-md-4')),
                    css_class='col-md-6'),
                Div(
                    'Servicio',
                    'Mterreno',
                    'Mconstruccion',
                    
                    'Cliente', css_class='col-md-3'),
                Div(
                    'Depto',
                    'Valuador',
                    'Valor',
                    'Solicitud',
                    css_class='col-md-3'),
                css_class='row-fluid'),
            'Observaciones',
            ButtonHolder(
                Submit('submit',  'Enviar',  css_class='btn-success')
            ))
        super(AltaAvaluo,  self).__init__(*args,  **kwargs)
        self.fields['Municipio'] = forms.ModelChoiceField(queryset=Municipio.objects.filter(estado_id__is_active='True'))
        self.fields['Depto'] = forms.ModelChoiceField(queryset=Depto.objects.filter(is_active='True'))


################################
## Plain 'ole Formset example ##
################################

class FormaSencillaPaquete(forms.Form):
    Referencia = forms.CharField(required=False, label="Expediente Catastral")
    # Calle = forms.CharField()
    NumExt = forms.CharField(label="Num. Ext.", required=False)
    NumInt = forms.CharField(label="Num. Int.", required=False)
    Colonia = forms.CharField()
    Tipo = forms.ModelChoiceField(required=True, label="Tipo Inmueble",  queryset=Tipo.objects.all())
    Municipio = forms.ModelChoiceField(queryset=Municipio.objects.filter(estado_id__is_active='True'))
    Estado = forms.ModelChoiceField(queryset=Estado.objects.filter(is_active='True'))
    Servicio = forms.ChoiceField(choices=SERVICIOS, label="Tipo Servicio")
    Estatus = forms.ChoiceField(choices=ESTATUS)
    Prioridad = forms.ChoiceField(choices=PRIORIDAD)
    Cliente = forms.ModelChoiceField(queryset=Cliente.objects.all())
    Depto = forms.ModelChoiceField(queryset=Depto.objects.filter(is_active='True'))
    Solicitud = forms.DateField(label="Fecha Solicitud", widget=forms.DateInput(format='%d/%m/%Y'),  input_formats=['%d/%m/%Y'])
    Observaciones = forms.CharField(widget=forms.Textarea, required=False)
    Valor = forms.DecimalField(required=False, widget=forms.TextInput())
    Valuador = forms.ModelChoiceField(queryset=Valuador.objects.filter(is_active='True'))

    class Meta:
        model = Avaluo
        exclude = ('avaluo_id', 'FolioK', 'LatitudG', 'LatitudM', 'LatitudS', 'LongitudG', 'LongitudM', 'LongitudS', 
                   'Mterreno', 'Mconstruccion', 'Visita', 'Gastos', 'Importe', 'Salida', 'Pagado', 'Factura','Declat','Declon',
                   'Referencia','NumExt','NumInt','Calle')
    def clean_Referencia(self):
        return self.cleaned_data['Referencia'] or None
    def __init__(self,  *args,  **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_tag = False
        self.helper.layout = Layout(
                        Div(
                            'Tipo',
                            'Servicio',
                            'Cliente',
                            css_class='col-md-3'),
                        Div(
                            'Depto',
                            'Colonia',
                            'Estado',
                            
                            css_class='col-md-3'),
                        Div(
                            'Municipio',
                            'Estatus',
                            'Prioridad',

                            css_class='col-md-3'),
                        Div( 
                            'Valuador'  ,                                        
                            'Valor',
                            'Solicitud',
                            css_class='col-md-3'))
        super(FormaSencillaPaquete,  self).__init__(*args,  **kwargs)
        self.fields['Municipio'] = forms.ModelChoiceField(queryset=Municipio.objects.filter(estado_id__is_active='True'))
        self.fields['Depto'] = forms.ModelChoiceField(queryset=Depto.objects.filter(is_active='True'))

class FormaPaquete(forms.Form):
    Referencia = forms.CharField(required=False, label="Expediente Catastral")
    Calle = forms.CharField(required=True)
    NumExt = forms.CharField(label="Num. Ext.", required=False)
    NumInt = forms.CharField(label="Num. Int.", required=False)
    class Meta:
        model = Avaluo
        fields = ('Referencia','NumExt','NumInt','Calle')
    def clean_Referencia(self):
        if Avaluo.objects.filter(Referencia=self.cleaned_data['Referencia']).count() > 0:
            raise forms.ValidationError("Ya existe un Avaluo con esta Referencia.")
        else:
            return self.cleaned_data['Referencia'] or None
    def __init__(self,  *args,  **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_tag = False
        self.helper.layout = Layout(
                Div(
                    'Referencia',
                    css_class='col-md-3'),
                Div(
                    'Calle',
                    css_class='col-md-3'),
                Div(
                    'NumExt',
                    css_class='col-md-3'),
                Div('NumInt',
                    css_class='col-md-3'))
        super(FormaPaquete,  self).__init__(*args,  **kwargs)
PaqueteFormset = formsets.formset_factory(FormaPaquete,can_delete=True, extra=1)
# Define the same formset, with no forms (so we can demo the form template):
EmptyPaqueteFormset = formsets.formset_factory(FormaPaquete, extra=0)


class VisitaAvaluo(ModelForm):
    Calle = forms.CharField( )
    NumExt = forms.CharField( label="Num. Ext.", required=False)
    NumInt = forms.CharField( label="Num. Int.", required=False)
    Estatus = forms.ChoiceField( choices=ESTATUSV)
    Visita = forms.DateField(label="Fecha Visita", widget=forms.DateInput(format='%d/%m/%Y'),  input_formats=['%d/%m/%Y'])
    Tipo = forms.ModelChoiceField(queryset=Tipo.objects.filter(is_active='True'),label="Tipo de Bien")
    Lote_Tipo = forms.CharField( label="Tipo de Lote", required=False)
    LatitudG = forms.DecimalField(required=False, label="Lon.G.")
    LatitudM = forms.DecimalField(required=False, label="Lon.M.",)
    LatitudS = forms.DecimalField(required=False, label="Lon.S.")
    LongitudG = forms.DecimalField(required=False, label="Lat.G.")
    LongitudM = forms.DecimalField(required=False, label="Lat.M.")
    LongitudS = forms.DecimalField(required=False, label="Lat.S.")
    Mterreno = forms.DecimalField(required=False, label="Mts. Terreno")
    Mconstruccion = forms.DecimalField(required=False, label="Mts. Construcción")
    Factor_Terreno = forms.DecimalField( label="Fct.", required=True)
    Factor_Construccion = forms.DecimalField( label="Fct.", required=True)
    Valor_Mterreno = forms.DecimalField( label="Val.M.Terreno", required=True)
    Valor_Mconstruccion = forms.DecimalField( label="Val.M.Constr.", required=True)
    Valor_Terreno_Concluido = forms.DecimalField( label="Va.T.Concluido", required=True)
    Valor_Construccion_Concluido = forms.DecimalField( label="Val.C.Concluido", required=True)
    Observaciones = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Avaluo
        exclude = ('avaluo_id', 'Solicitud', 'Folio', 'Referencia', 'Prioridad', 'Colonia', 
                   'Municipio', 'Estado', 'Servicio', 'Salida', 'Factura', 'Cliente', 'Depto', 
                   'Valuador', 'Solicitud', 'Valor', 'Gastos', 
                   'Importe', 'Pagado','Contacto','Declat','Declon')
    def clean_Referencia(self):
        return self.cleaned_data['Referencia'] or None
    def __init__(self,  *args,  **kwargs):
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
                    'Tipo',
                    css_class='col-md-3'),
                Div(
                    'Visita',
                    'Estatus',
                    'Mterreno',
                    'Mconstruccion',
                    css_class='col-md-3'),
                Div(
                    Div(
                        Div(Field('LongitudG',  css_class='span16 input-medium'),  css_class='col-md-4'),
                        Div(Field('LongitudM',  css_class='span16 input-medium'),  css_class='col-md-4'),
                        Div(Field('LongitudS',  css_class='span16 input-medium'),  css_class='col-md-4')),
                    Div(
                        Div(Field('LatitudG',  css_class='span20 input-large'),  css_class='col-md-4'),
                        Div(Field('LatitudM',  css_class='span16 input-medium'),  css_class='col-md-4'),
                        Div(Field('LatitudS',  css_class='span16 input-medium'),  css_class='col-md-4')),
                     Div(
                        Div(Field('Valor_Mterreno',  css_class='col-md-4'),  css_class='col-md-4'),
                        Div(Field('Factor_Terreno',  css_class='col-md-2'),  css_class='col-md-3'),
                        Div(HTML("""<h3>=</h3>"""),  css_class='col-md-1'),
                        Div(Field('Valor_Terreno_Concluido',  css_class='col-md-5'),  css_class='col-md-4')),
                     Div(
                        Div(Field('Valor_Mconstruccion',  css_class='col-md-5'),  css_class='col-md-4'),
                        Div(Field('Factor_Construccion',  css_class='col-md-1'),  css_class='col-md-3'),
                        Div(HTML("""<h3>=</h3>"""),  css_class='col-md-1'),
                        Div(Field('Valor_Construccion_Concluido',  css_class='col-md-5'),  css_class='col-md-4')),
                    css_class='col-md-6'), css_class='row-fluid'),
            'Observaciones',
            ButtonHolder(
                Submit('submit',  'Enviar',  css_class='btn-success')
            ))
        super(VisitaAvaluo,  self).__init__(*args,  **kwargs)
        for k, field in self.fields.items():
            if 'required' in field.error_messages:
                field.error_messages['required'] = ''



class CapturaAvaluo(ModelForm):

    Calle = forms.CharField()
    Calle = forms.CharField(required="True")
    NumExt = forms.CharField(label="Num. Ext.", required=False)
    NumInt = forms.CharField(label="Num. Int.", required=False)
    Colonia = forms.CharField()
    Municipio = forms.ModelChoiceField( queryset=Municipio.objects.filter(estado_id__is_active='True'))
    Servicio = forms.ModelChoiceField( queryset=Servicio.objects.filter(is_active='True'))
    Estado = forms.ModelChoiceField( queryset=Estado.objects.filter(is_active='True'))
    Tipo = forms.ModelChoiceField(queryset=Tipo.objects.filter(is_active='True'),label="Tipo de Bien")
    Estatus = forms.ChoiceField(choices=ESTATUS)
    #Prioridad = forms.ChoiceField(choices=PRIORIDAD)
    Referencia = forms.CharField(required=False, label="Expediente Catastral")
    Solicitud = forms.DateField(label="Fecha Solicitud", widget=forms.DateInput(format='%d/%m/%Y'),  input_formats=['%d/%m/%Y'])
    Mterreno = forms.DecimalField(required=False)
    Mconstruccion = forms.DecimalField(required=False)
    LatitudG = forms.DecimalField(required=False, label="Lon.G.")
    LatitudM = forms.DecimalField(required=False, label="Lon.M.")
    LatitudS = forms.DecimalField(required=False, label="Lon.S.")
    LongitudG = forms.DecimalField(required=False, label="Lat.G.")
    LongitudM = forms.DecimalField(required=False, label="Lat.M.")
    LongitudS = forms.DecimalField(required=False, label="Lat.S.")
    Valor = forms.DecimalField(required=True,  widget=forms.TextInput())
    Gastos = forms.DecimalField(required=False,  widget=forms.TextInput())
    Importe = forms.DecimalField(required=False,  widget=forms.TextInput())
    Observaciones = forms.CharField(widget=forms.Textarea, required=False)
   # Valuador = forms.ModelChoiceField(queryset=Valuador.objects.filter(is_active='True'))

    class Meta:
        model = Avaluo
        exclude = ('Salida', 'Visita', 'Pagado', 'Cliente', 'Depto', 'Factura', 'Folio','Valuador','Declat','Declon','Prioridad')
    def clean_Referencia(self):
        return self.cleaned_data['Referencia'] or None
    def __init__(self,  *args,  **kwargs):
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
                    
                    css_class='col-md-3'),
                Div(
                    'Municipio',
                    'Estado',
                    'Servicio',
                    'Tipo',
                    'Estatus',
                    #'Prioridad',
                    #'Valuador',
                    css_class='col-md-3'),
                Div(
                    Div(
                        Div(Field('LongitudG',  css_class='span16 input-medium'),  css_class='col-md-4'),
                        Div(Field('LongitudM',  css_class='span16 input-medium'),  css_class='col-md-4'),
                        Div(Field('LongitudS',  css_class='span16 input-medium'),  css_class='col-md-4')),
                    Div( 
                        Div(Field('LatitudG',  css_class='span20 input-large'),  css_class='col-md-4'),
                        Div(Field('LatitudM',  css_class='span16 input-medium'),  css_class='col-md-4'),
                        Div(Field('LatitudS',  css_class='span16 input-medium'),  css_class='col-md-4')),
                    css_class='col-md-4'),
                Div('Solicitud',
                    'Mterreno',
                    'Mconstruccion',
                    css_class='col-md-3'),
                Div(
                    'Valor',
                    'Gastos',
                    'Importe',
                    css_class='col-md-3'),
                css_class='row-fluid'),
            'Observaciones',
            ButtonHolder(
                Submit('submit',  'Enviar',  css_class='btn-success')
            ))
        super(CapturaAvaluo,  self).__init__(*args,  **kwargs)
        self.fields['Municipio'] = forms.ModelChoiceField(queryset=Municipio.objects.filter(estado_id__is_active='True'))
class SalidaAvaluo(ModelForm):
    Referencia = forms.CharField(required=True, label="Expediente Catastral")
    Mterreno = forms.DecimalField(required=True, widget=forms.TextInput())
    Gastos = forms.DecimalField(required=True, widget=forms.TextInput())
    Mconstruccion = forms.DecimalField(required=True, widget=forms.TextInput())
    Observaciones = forms.CharField(widget=forms.Textarea, required=False)
    Salida = forms.DateField(label="Fecha Salida", widget=forms.DateInput(format='%d/%m/%Y'),  input_formats=['%d/%m/%Y'])
    Valor = forms.DecimalField(required=True, widget=forms.TextInput())
    Importe = forms.DecimalField(required=True, widget=forms.TextInput(),  max_value=100000)

    class Meta:
        model = Avaluo
        fields = ('Mterreno', 'Mconstruccion', 'Observaciones', 'Salida', 'Importe', 'Referencia','Valor','Gastos','Factura',)
    def clean_Referencia(self):
        return self.cleaned_data['Referencia'] or None
    def __init__(self,  *args,  **kwargs):
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
                    css_class='col-md-4'),
                Div('Solicitud',
                    'Mterreno',
                    'Mconstruccion',
                    'Factura',
                    css_class='col-md-4'),
                Div('Valor',
                    'Importe',
                    css_class='col-md-4'),
                Div('Gastos',
                    css_class='col-md-4'),
                css_class='row-fluid'),
            'Observaciones',
            ButtonHolder(
                Submit('submit',  'Enviar',  css_class='btn-success')
            ))
        super(SalidaAvaluo,  self).__init__(*args,  **kwargs)


class FormaConsultaMaster(ModelForm):
    FolioK = forms.CharField(required=False, label="Folio")
    Referencia = forms.CharField(required=False, label="Expediente Catastral")
    Calle = forms.CharField(required=False)
    #NumExt = forms.CharField(label="Num. Ext.", required=False)
    #NumInt = forms.CharField(label="Num. Int.", required=False)
    Colonia = forms.CharField(required=False)
    Municipio = forms.ModelChoiceField(required=False,   queryset=Municipio.objects.filter(estado_id__is_active='True'))
    Estado = forms.ModelChoiceField(required=False,   queryset=Estado.objects.filter(is_active='True'))
    #Servicio = forms.CharField(required=False, label="Tipo.Servicio")
    Tipo = forms.ModelChoiceField(required=False, label="Tipo Inmueble",  queryset=Tipo.objects.all())
    Estatus = forms.MultipleChoiceField(choices=ESTATUS, required=False, widget=forms.CheckboxSelectMultiple,)
    Valuador = forms.ModelChoiceField(required=False,  queryset=Valuador.objects.all())
    Prioridad = forms.ChoiceField(choices=PRIORIDAD, required=False)
    Referencia = forms.CharField(required=False)
    Solicitud = forms.DateField(label="Fecha Solicitud", widget=forms.DateInput(format='%d/%m/%Y'), input_formats=['%d/%m/%Y'], required=False)
    Visita = forms.DateField(label="Fecha Visita", widget=forms.DateInput(format='%d/%m/%Y'), input_formats=['%d/%m/%Y'], required=False)
    Mterreno = forms.DecimalField(required=False)
    Mconstruccion = forms.DecimalField(required=False)
    LatitudG = forms.DecimalField(required=False, label="Lon.G.")
    LatitudM = forms.DecimalField(required=False, label="Lon.M.")
    LatitudS = forms.DecimalField(required=False, label="Lon.S.")
    LongitudG = forms.DecimalField(required=False, label="Lat.G.")
    LongitudM = forms.DecimalField(required=False, label="Lat.M.")
    LongitudS = forms.DecimalField(required=False, label="Lat.S.")
    Valor = forms.DecimalField(required=False, widget=forms.TextInput())
    Gastos = forms.DecimalField(required=False, widget=forms.TextInput())
    Importe = forms.DecimalField(required=False, widget=forms.TextInput())
    Observaciones = forms.CharField(widget=forms.Textarea, required=False)
    Mes = forms.ChoiceField( choices=MESES, required=False)
    Anio = forms.ChoiceField(choices=[], required=False)
    Factura = forms.CharField(required=False)

    class Meta:
        model = Avaluo
        exclude = ('Salida', 'Prioridad', 'Pagado','NumExt','NumInt','Servicio','Declat','Declon')
    def clean(self):
        cleaned_data = self.cleaned_data
        ref = cleaned_data.get('Referencia')
        if ref in self._errors:
            del self._errors['Referencia']
        return self.cleaned_data 
    def clean_Referencia(self):
        return self.cleaned_data['Referencia'] or None
    def __init__(self,  *args,  **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-FormaConsultaMaster'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Div(
                    'Fecha:',
                    'Mes',
                    'Anio',
                    Field('Estatus',id='id_estatus'),
                    css_class='col-md-3'),
                Div(
                    'Edita Avaluo - Captura',
                    'FolioK',
                    'Referencia',
                    'Calle',
                    'Cliente',
                    css_class='col-md-3'),
                Div(
                    'Colonia',
                    'Estado',
                    'Municipio',
                    'Depto',
                    css_class='col-md-3'),
                Div(
                    'Tipo',
                    'Valor',
                    'Factura',
                    'Importe',
                     
                    css_class='col-md-3'), css_class='row-fluid'),
            ButtonHolder(
                #Submit('Buscar',  'Buscar',  css_class='button white'),
            ))
        super(FormaConsultaMaster,  self).__init__(*args,  **kwargs)
        self.fields['Municipio'] = forms.ModelChoiceField(required=False,  queryset=Municipio.objects.filter(estado_id__is_active='True'))
        year = datetime.datetime.now().year
        anios = Avaluo.objects.all().dates('Salida', 'year')[0].year
        self.fields['Anio'].choices = [('','')]
        self.fields['Anio'].choices += [(i, i) for i in range(anios, year+1)]

class RespuestaConsultaMaster(ModelForm):
    FolioK = forms.CharField( required=False)
    Referencia = forms.CharField(required=False, label="Expediente Catastral")
    Calle = forms.CharField( required=False)
    NumExt = forms.CharField( label="Num. Ext.", required=False)
    NumInt = forms.CharField( label="Num. Int.", required=False)
    Colonia = forms.CharField( required=False)
    Municipio = forms.ModelChoiceField( queryset=Municipio.objects.filter(estado_id__is_active='True'))
    Estado = forms.ModelChoiceField( queryset=Estado.objects.filter(is_active='True'))
    Servicio = forms.ChoiceField( choices=SERVICIOS, label="Tipo Servicio")
    Estatus = forms.ChoiceField( choices=ESTATUS, required=False)
    Valuador = forms.ModelChoiceField(required=False,  queryset=Valuador.objects.all())
    Prioridad = forms.ChoiceField( choices=PRIORIDAD, required=False)
    Referencia = forms.CharField( required=False)
    Solicitud = forms.DateField(label="Fecha Solicitud", widget=forms.DateInput(format='%d/%m/%Y'),  input_formats=['%d/%m/%Y'], required=False)
    Visita = forms.DateField(label="Fecha Visita", widget=forms.DateInput(format='%d/%m/%Y'),  input_formats=['%d/%m/%Y'], required=False)
    Salida = forms.DateField(label="Fecha Salida", widget=forms.DateInput(format='%d/%m/%Y'),  input_formats=['%d/%m/%Y'], required=False)
    Mterreno = forms.DecimalField(required=False)
    Mconstruccion = forms.DecimalField(required=False)
    LatitudG = forms.DecimalField(required=False, label="Lon.G.")
    LatitudM = forms.DecimalField(required=False, label="Lon.M.")
    LatitudS = forms.DecimalField(required=False, label="Lon.S.")
    LongitudG = forms.DecimalField(required=False, label="Lat.G.")
    LongitudM = forms.DecimalField(required=False, label="Lat.M.")
    LongitudS = forms.DecimalField(required=False, label="Lat.S.")
    Cliente = forms.ModelChoiceField( queryset=Cliente.objects.all())
    #Depto = forms.ModelChoiceField(required=False, queryset=Depto.objects.filter(is_active='False'))
    Valor = forms.DecimalField(required=False, widget=forms.TextInput())
    Gastos = forms.DecimalField(required=False, widget=forms.TextInput())
    Importe = forms.DecimalField(required=False, widget=forms.TextInput())
    Observaciones = forms.CharField(widget=forms.Textarea, required=False)
    Factura = forms.CharField( required=False)
    Pagado = forms.BooleanField(required=False)
    class Meta:
        model = Avaluo
        exclude = ('Declat','Declon',)
    def clean_Referencia(self):
        return self.cleaned_data['Referencia'] or None
    def __init__(self,  *args,  **kwargs):

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
                    'Cliente',
                    css_class='col-md-3'),
                Div(
                    'Estado',
                    'Municipio',
                    'Servicio',
                    'Estatus',
                    'Valuador',
                    'Depto',
                    'Visita',
                    css_class='col-md-3'),
                Div(
                    Div(
                        Div(Field('LatitudG',  css_class='col-md-20 input-small'),  css_class='col-md-4'),
                        Div(Field('LatitudM',  css_class='col-md-20 input-small'),  css_class='col-md-4'),
                        Div(Field('LatitudS',  css_class='col-md-20 input-small'),  css_class='col-md-4')),
                    Div(
                        Div(Field('LongitudG',  css_class='col-md-20 input-small'),  css_class='col-md-4'),
                        Div(Field('LongitudM',  css_class='col-md-20 input-small'),  css_class='col-md-4'),
                        Div(Field('LongitudS',  css_class='col-md-20 input-small'),  css_class='col-md-4')),
                    css_class='col-md-6'),
                Div(
                    'Salida',
                    'Mterreno',
                    'Mconstruccion',
                    'Valor',
                    css_class='col-md-3'),
                Div(
                    'Gastos',
                    'Solicitud',
                    'Importe',
                    'Prioridad',
                    'Factura',
                    'Pagado',
                    css_class='col-md-3'),
                css_class='row-fluid'),
            'Observaciones',
            ButtonHolder(
                Submit('submit',  'Guardar',  css_class='btn-success')
            ))


        super(RespuestaConsultaMaster,  self).__init__(*args,  **kwargs)
        if self.instance:
            estado = self.instance.Estado
            cliente = self.instance.Cliente
        self.fields['Municipio'] = forms.ModelChoiceField(queryset=Municipio.objects.filter(estado_id__is_active='True',estado_id=estado))
        self.fields['Depto'] = forms.ModelChoiceField(required=False, queryset=Depto.objects.filter(is_active='True'))

'''
class FormaConsultaSencilla(ModelForm):
    FolioK = forms.CharField(required=False)
    Calle = forms.CharField(required=False)
    NumExt = forms.CharField(label="Num. Ext.", required=False)
    NumInt = forms.CharField(label="Num. Int.", required=False)
    Colonia = forms.CharField(required=False)
    Municipio = forms.ModelChoiceField(queryset=Municipio.objects.filter(estado_id__is_active='True'), required=False)
    Estado = forms.ModelChoiceField(queryset=Estado.objects.filter(is_active='True'), required=False)
    Servicio = forms.CharField(required=False, label="Tipo.Servicio")
    Tipo = forms.ModelChoiceField(required=False, queryset=Tipo.objects.all())
    Estatus = forms.ChoiceField(choices=ESTATUS, required=False)
    Valuador = forms.ModelChoiceField(required=False, queryset=Valuador.objects.all())
    Prioridad = forms.ChoiceField(choices=PRIORIDAD, required=False)
    Referencia = forms.CharField(required=False)
    Solicitud = forms.DateField(label="Fecha Solicitud", widget=forms.DateInput(format='%d/%m/%Y'),  input_formats=['%d/%m/%Y'], required=False)
    Visita = forms.DateField(label="Fecha Visita", widget=forms.DateInput(format='%d/%m/%Y'),  input_formats=['%d/%m/%Y'], required=False)
    Mterreno = forms.DecimalField(required=False)
    Mconstruccion = forms.DecimalField(required=False)
    LatitudG = forms.DecimalField(required=False, label="Lon.G.")
    LatitudM = forms.DecimalField(required=False, label="Lon.M.")
    LatitudS = forms.DecimalField(required=False, label="Lon.S.")
    LongitudG = forms.DecimalField(required=False, label="Lat.G.")
    LongitudM = forms.DecimalField(required=False, label="Lat.M.")
    LongitudS = forms.DecimalField(required=False, label="Lat.S.")
    Valor = forms.DecimalField(required=False, widget=forms.TextInput())
    Gastos = forms.DecimalField(required=False, widget=forms.TextInput())
    Importe = forms.DecimalField(required=False, widget=forms.TextInput())
    Observaciones = forms.CharField(widget=forms.Textarea, required=False)
    Mes = forms.ChoiceField( choices=MESES, required=False)
    Anio = forms.ChoiceField(choices=[], required=False)

    class Meta:
        model = Avaluo
        exclude = ('Salida', 'Pagado', 'Cliente', 'Depto', 'Factura', 'Prioridad','Declat','Declon')
    def clean(self):
        cleaned_data = self.cleaned_data
        ref = cleaned_data.get('Referencia')
        if ref in self._errors:
            del self._errors['Referencia']
        return self.cleaned_data 
    def clean_Referencia(self):
        return self.cleaned_data['Referencia'] or None
    def __init__(self,  *args,  **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-FormaConsultaSencilla'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        #self.helper.form_action='lista_consulta_sencilla'
        self.helper.layout = Layout(
            Div(
                Div(Fieldset
                    ('Fecha:',
                     'Mes',
                     'Anio'),
                    css_class='col-md-3'),
                Div(
                    'Edita Avaluo - Captura',
                    'FolioK',
                    'Referencia',
                    'Calle',
                    'NumExt',
                    'NumInt',
                    css_class='col-md-3'),
                Div(
                    'Colonia',
                    'Estado',
                    'Municipio',
                    'Servicio',
                    'Tipo',
                    css_class='col-md-3'),
                css_class='row-fluid'),
            ButtonHolder(
                Submit('Buscar', 'Buscar', css_class='btn-success'),
            ))
        super(FormaConsultaSencilla,  self).__init__(*args,  **kwargs)
        self.fields['Municipio'] = forms.ModelChoiceField(required=False,  queryset=Municipio.objects.filter(estado_id__is_active='True'))
        year = datetime.datetime.now().year
        anios = Avaluo.objects.all().dates('Salida', 'year')[0].year
        self.fields['Anio'].choices = [(i, i) for i in range(anios, year+1)]
'''





class FacturaForm(ModelForm):
    Factura = forms.CharField(label="Factura",required=True)

    class Meta:
        model = Avaluo
        fields = ('avaluo_id', 'Factura')

    def __init__(self,  *args,  **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-FacturaForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'POST'
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(Div('Factura',
                    css_class='col-md-3'),
                css_class='row'))
        super(FacturaForm,  self).__init__(*args,  **kwargs)


class EmptyForm(ModelForm):
    class Meta:
        model = Avaluo
        fields = ('avaluo_id',)

    def __init__(self,  *args,  **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-EmptyForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'POST'
        self.helper.form_tag = False
        super(EmptyForm,  self).__init__(*args,  **kwargs)

class VisitaMasiva(ModelForm):
    LatitudG = forms.DecimalField(required=True, label="Lon.G.")
    LatitudM = forms.DecimalField(required=True, label="Lon.M.")
    LatitudS = forms.DecimalField(required=True, label="Lon.S.")
    LongitudG = forms.DecimalField(required=True, label="Lat.G.")
    LongitudM = forms.DecimalField(required=True, label="Lat.M.")
    LongitudS = forms.DecimalField(required=True, label="Lat.S.")
    Visita = forms.DateField(label="Fecha Visita", widget=forms.DateInput(format='%d/%m/%Y'),  input_formats=['%d/%m/%Y'], required=True)

    class Meta:
        model = Avaluo
        fields = ('LatitudG', 'LatitudM', 'LatitudS', 'LongitudG', 'LongitudM', 'LongitudS','Visita')

    def __init__(self,  *args,  **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-VisitaMasiva'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'POST'
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(Div('LongitudG',
                    'LatitudG',
                    css_class='col-md-4'),
                Div('LongitudM',
                    'LatitudM',
                    css_class='col-md-4'),
                Div('LongitudS',
                    'LatitudS',
                    'Visita',
                    css_class='col-md-4'),
                css_class='row-fluid'))
        super(VisitaMasiva,  self).__init__(*args,  **kwargs)

class CapturaMasiva(ModelForm):
    Mterreno = forms.DecimalField(required=False, label="Mts. Terreno")
    Mconstruccion = forms.DecimalField(required=False, label="Mts. Construcción")
    class Meta:
        model = Avaluo
        fields = ('Mterreno', 'Mconstruccion')

    def __init__(self,  *args,  **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-CapturaMasiva'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'POST'
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(Div('Mterreno'),
                Div('Mconstruccion'),
                css_class='row'))
        super(CapturaMasiva,  self).__init__(*args,  **kwargs)

class SalidaMasiva(ModelForm):
    Valor = forms.DecimalField(required=True, widget=forms.TextInput())
    Gastos = forms.DecimalField(required=True, widget=forms.TextInput())
    Importe = forms.DecimalField(required=True, widget=forms.TextInput())
    Salida = forms.DateField(label="Fecha Salida", widget=forms.DateInput(format='%d/%m/%Y'),  input_formats=['%d/%m/%Y'])
    class Meta:
        model = Avaluo
        fields = ('Valor', 'Gastos','Importe','Salida')

    def __init__(self,  *args,  **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-SalidaMasiva'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'POST'
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(Div('Valor'),
                Div('Gastos'),
                Div(Field('Importe',css_id='id_Importe'),css_id='div_id_Importe'),
                Div('Salida'),
                css_class=''))
        super(SalidaMasiva,  self).__init__(*args,  **kwargs)

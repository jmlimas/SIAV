from app.models import *
from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper, reverse
from crispy_forms.layout import *


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
)

ESTATUSV = (
    ('PROCESO', 'PROCESO'),
    ('DETENIDO', 'DETENIDO'),
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


class AltaAvaluo(ModelForm):

    Referencia = forms.CharField(required=False)
    Calle = forms.CharField()
    NumExt = forms.CharField(label="Num. Ext.", required=False)
    NumInt = forms.CharField(label="Num. Int.", required=False)
    Colonia = forms.CharField()
    Municipio = forms.ModelChoiceField(queryset=Municipio.objects.filter(estado_id__is_active='True'))
    Estado = forms.ModelChoiceField(queryset=Estado.objects.filter(is_active='True'))
    Servicio = forms.ChoiceField(choices=SERVICIOS, label="Tipo Servicio")
    Estatus = forms.ChoiceField(choices=ESTATUS)
    Prioridad = forms.ChoiceField(choices=PRIORIDAD)
    Depto = forms.ModelChoiceField(queryset=Depto.objects.filter(is_active='True'))
    Solicitud = forms.DateField(label="Fecha Solicitud", widget=forms.DateInput(format='%d/%m/%Y'),  input_formats=['%d/%m/%Y'])
    Observaciones = forms.CharField(widget=forms.Textarea, required=False)
    Valor = forms.DecimalField(required=False)
    Valuador = forms.ModelChoiceField(queryset=Valuador.objects.filter(is_active='True'))

    class Meta:
        model = Avaluo
        exclude = ('avaluo_id', 'FolioK', 'LatitudG', 'LatitudM', 'LatitudS', 'LongitudG', 'LongitudM', 'LongitudS', 'Mterreno', 'Mconstruccion', 'Visita', 'Gastos', 'Importe', 'Salida', 'Pagado', 'Factura', )
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
                    'NumExt', css_class='span3'),
                Div(
                    'NumInt',
                    'Colonia',
                    'Estado',
                    'Municipio', css_class='span3'),
                Div(
                    'Servicio',
                    'Estatus',
                    'Prioridad',
                    'Cliente', css_class='span3'),
                Div(
                    'Depto',
                    'Valuador',
                    'Valor',
                    'Solicitud',
                    css_class='span3'),
                css_class='row-fluid'),
            'Observaciones',
            ButtonHolder(
                Submit('submit',  'Enviar',  css_class='btn-success')
            ))
        super(AltaAvaluo,  self).__init__(*args,  **kwargs)
        self.fields['Municipio'] = forms.ModelChoiceField(queryset=Municipio.objects.filter(estado_id__is_active='True'))
        self.fields['Depto'] = forms.ModelChoiceField(queryset=Depto.objects.all())

class VisitaAvaluo(ModelForm):
    Calle = forms.CharField( )
    NumExt = forms.CharField( label="Num. Ext.", required=False)
    NumInt = forms.CharField( label="Num. Int.", required=False)
    Estatus = forms.ChoiceField( choices=ESTATUSV)
    Visita = forms.DateField(label="Fecha Visita", widget=forms.DateInput(format='%d/%m/%Y'),  input_formats=['%d/%m/%Y'])
    LatitudG = forms.DecimalField(required=True, label="Lon.G.")
    LatitudM = forms.DecimalField(required=True, label="Lon.M.",)
    LatitudS = forms.DecimalField(required=True, label="Lon.S.")
    LongitudG = forms.DecimalField(required=True, label="Lat.G.")
    LongitudM = forms.DecimalField(required=True, label="Lat.M.")
    LongitudS = forms.DecimalField(required=True, label="Lat.S.")
    Observaciones = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Avaluo
        exclude = ('avaluo_id', 'Solicitud', 'FolioK', 'Referencia', 'Prioridad', 'Colonia', 'Municipio', 'Estado', 'Servicio', 'Salida', 'Factura', 'Cliente', 'Depto', 'Valuador', 'Solicitud', 'Mterreno', 'Mconstruccion', 'Valor', 'Gastos', 'Importe', 'Pagado')
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
                    css_class='span3'),
                Div(
                    'Visita',
                    'Estatus',
                    'Tipo',
                    css_class='span3'),
                Div(
                    Div(
                        Div(Field('LatitudG',  css_class='span20 input-large'),  css_class='span4'),
                        Div(Field('LatitudM',  css_class='span16 input-medium'),  css_class='span4'),
                        Div(Field('LatitudS',  css_class='span16 input-medium'),  css_class='span4')),
                    Div(
                        Div(Field('LongitudG',  css_class='span16 input-medium'),  css_class='span4'),
                        Div(Field('LongitudM',  css_class='span16 input-medium'),  css_class='span4'),
                        Div(Field('LongitudS',  css_class='span16 input-medium'),  css_class='span4')),
                    css_class='span4'), css_class='row-fluid'),
            'Observaciones',
            ButtonHolder(
                Submit('submit',  'Enviar',  css_class='btn-success')
            ))
        super(VisitaAvaluo,  self).__init__(*args,  **kwargs)


class CapturaAvaluo(ModelForm):

    Calle = forms.CharField()
    Calle = forms.CharField(required="True")
    NumExt = forms.CharField(label="Num. Ext.", required=False)
    NumInt = forms.CharField(label="Num. Int.", required=False)
    Colonia = forms.CharField()
    Municipio = forms.ModelChoiceField( queryset=Municipio.objects.filter(estado_id__is_active='True'))
    Estado = forms.ModelChoiceField( queryset=Estado.objects.filter(is_active='True'))
    Estatus = forms.ChoiceField(choices=ESTATUS)
    Prioridad = forms.ChoiceField(choices=PRIORIDAD)
    Referencia = forms.CharField(required=False)
    Solicitud = forms.DateField(label="Fecha Solicitud", widget=forms.DateInput(format='%d/%m/%Y'),  input_formats=['%d/%m/%Y'])
    Mterreno = forms.DecimalField(required=False)
    Mconstruccion = forms.DecimalField(required=False)
    LatitudG = forms.DecimalField(required=False, label="Lon.G.")
    LatitudM = forms.DecimalField(required=False, label="Lon.M.")
    LatitudS = forms.DecimalField(required=False, label="Lon.S.")
    LongitudG = forms.DecimalField(required=False, label="Lat.G.")
    LongitudM = forms.DecimalField(required=False, label="Lat.M.")
    LongitudS = forms.DecimalField(required=False, label="Lat.S.")
    #Valor = forms.DecimalField(required=False)
    #Gastos = forms.DecimalField(required=False)
    #Importe = forms.DecimalField(required=False)
    Observaciones = forms.CharField(widget=forms.Textarea, required=False)
    Valuador = forms.ModelChoiceField(queryset=Valuador.objects.filter(is_active='True'))

    class Meta:
        model = Avaluo
        exclude = ('Salida', 'Visita', 'Pagado', 'Cliente', 'Depto', 'Factura', 'FolioK','Valor','Gastos','Importe')
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
                    'Estado',
                    css_class='span3'),
                Div(
                    'Municipio',
                    'Servicio',
                    'Tipo',
                    'Estatus',
                    'Prioridad',
                    'Valuador',
                    css_class='span3'),
                Div(
                    Div(
                        Div(Field('LatitudG',  css_class='span20 input-large'),  css_class='span4'),
                        Div(Field('LatitudM',  css_class='span16 input-medium'),  css_class='span4'),
                        Div(Field('LatitudS',  css_class='span16 input-medium'),  css_class='span4')),
                    Div(
                        Div(Field('LongitudG',  css_class='span16 input-medium'),  css_class='span4'),
                        Div(Field('LongitudM',  css_class='span16 input-medium'),  css_class='span4'),
                        Div(Field('LongitudS',  css_class='span16 input-medium'),  css_class='span4')),
                    css_class='span4'),
                Div('Solicitud',
                    'Mterreno',
                    'Mconstruccion',
                    css_class='span3'),
                Div(
                    #'Valor',
                    #'Gastos',
                    #'Importe',
                    css_class='span3'),
                css_class='row-fluid'),
            'Observaciones',
            ButtonHolder(
                Submit('submit',  'Enviar',  css_class='btn-success')
            ))
        super(CapturaAvaluo,  self).__init__(*args,  **kwargs)
        self.fields['Municipio'] = forms.ModelChoiceField(queryset=Municipio.objects.filter(estado_id__is_active='True'))

class SalidaAvaluo(ModelForm):
    Referencia = forms.CharField(required=True)
    Mterreno = forms.DecimalField(required=True)
    Gastos = forms.DecimalField(required=True)
    Mconstruccion = forms.DecimalField(required=True)
    Observaciones = forms.CharField(widget=forms.Textarea, required=False)
    Salida = forms.DateField(label="Fecha Salida", widget=forms.DateInput(format='%d/%m/%Y'),  input_formats=['%d/%m/%Y'])
    Valor = forms.DecimalField(required=True)
    Importe = forms.DecimalField(required=True)

    class Meta:
        model = Avaluo
        fields = ('Mterreno', 'Mconstruccion', 'Observaciones', 'Salida', 'Importe', 'Referencia','Valor','Gastos')
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
                    css_class='span3'),
                Div('Solicitud',
                    'Mterreno',
                    'Mconstruccion',
                    css_class='span3'),
                Div('Valor',
                    'Importe',
                    css_class='span3'),
                Div('Gastos',
                    css_class='span3'),
                css_class='row-fluid'),
            'Observaciones',
            ButtonHolder(
                Submit('submit',  'Enviar',  css_class='btn-success')
            ))
        super(SalidaAvaluo,  self).__init__(*args,  **kwargs)


class FormaConsultaMaster(ModelForm):
    FolioK = forms.CharField(required=False)
    Calle = forms.CharField(required=False)
    #NumExt = forms.CharField(label="Num. Ext.", required=False)
    #NumInt = forms.CharField(label="Num. Int.", required=False)
    Colonia = forms.CharField(required=False)
    Municipio = forms.ModelChoiceField(required=False,   queryset=Municipio.objects.filter(estado_id__is_active='True'))
    Estado = forms.ModelChoiceField(required=False,   queryset=Estado.objects.filter(is_active='True'))
    #Servicio = forms.CharField(required=False, label="Tipo.Servicio")
    Tipo = forms.ModelChoiceField(required=False, label="Tipo Inmueble",  queryset=Tipo.objects.all())
    Estatus = forms.ChoiceField(choices=ESTATUS, required=False)
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
    Valor = forms.DecimalField(required=False)
    Gastos = forms.DecimalField(required=False)
    Importe = forms.DecimalField(required=False)
    Observaciones = forms.CharField(widget=forms.Textarea, required=False)
    Mes = forms.ChoiceField( choices=MESES, required=False)
    Anio = forms.ChoiceField( choices=ANIOS, required=False)
    Factura = forms.CharField(required=False)

    class Meta:
        model = Avaluo
        exclude = ('Salida', 'Prioridad', 'Pagado','NumExt','NumInt','Servicio')
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
                    css_class='span3'),
                Div(
                    'Edita Avaluo - Captura',
                    'FolioK',
                    'Referencia',
                    'Calle',
                    'Cliente',
                    css_class='span3'),
                Div(
                    'Colonia',
                    'Estado',
                    'Municipio',
                    'Depto',
                    css_class='span3'),
                Div(
                    'Tipo',
                    'Factura',
                    'Importe',
                    css_class='span3'), css_class='row-fluid'),
            ButtonHolder(
                #Submit('Buscar',  'Buscar',  css_class='button white'),
            ))
        super(FormaConsultaMaster,  self).__init__(*args,  **kwargs)
        self.fields['Municipio'] = forms.ModelChoiceField(required=False,  queryset=Municipio.objects.filter(estado_id__is_active='True'))


class RespuestaConsultaMaster(ModelForm):
    FolioK = forms.CharField( required=False)
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
    Valor = forms.DecimalField(required=False)
    Gastos = forms.DecimalField(required=False)
    Importe = forms.DecimalField(required=False)
    Observaciones = forms.CharField(widget=forms.Textarea, required=False)
    Factura = forms.CharField( required=False)
    Pagado = forms.BooleanField(required=False)

    class Meta:
        model = Avaluo
        exclude = ('',)
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
                    css_class='span3'),
                Div(
                    'Estado',
                    'Municipio',
                    'Servicio',
                    'Estatus',
                    'Valuador',
                    'Depto',
                    'Visita',
                    css_class='span3'),
                Div(
                    Div(
                        Div(Field('LatitudG',  css_class='span20 input-large'),  css_class='span4'),
                        Div(Field('LatitudM',  css_class='span16 input-medium'),  css_class='span4'),
                        Div(Field('LatitudS',  css_class='span16 input-medium'),  css_class='span4')),
                    Div(
                        Div(Field('LongitudG',  css_class='span16 input-medium'),  css_class='span4'),
                        Div(Field('LongitudM',  css_class='span16 input-medium'),  css_class='span4'),
                        Div(Field('LongitudS',  css_class='span16 input-medium'),  css_class='span4')),
                    css_class='span4'),
                Div(
                    'Salida',
                    'Mterreno',
                    'Mconstruccion',
                    'Valor',
                    css_class='span3'),
                Div(
                    'Gastos',
                    'Solicitud',
                    'Importe',
                    'Prioridad',
                    'Factura',
                    'Pagado',
                    css_class='span3'),
                css_class='row-fluid'),
            'Observaciones',
            ButtonHolder(
                Submit('submit',  'Guardar',  css_class='btn-success')
            ))
        super(RespuestaConsultaMaster,  self).__init__(*args,  **kwargs)
        self.fields['Municipio'] = forms.ModelChoiceField(queryset=Municipio.objects.filter(estado_id__is_active='True'))
        self.fields['Depto'] = forms.ModelChoiceField(queryset=Depto.objects.all())


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
    Valor = forms.DecimalField(required=False)
    Gastos = forms.DecimalField(required=False)
    Importe = forms.DecimalField(required=False)
    Observaciones = forms.CharField(widget=forms.Textarea, required=False)
    Mes = forms.ChoiceField( choices=MESES, required=False)
    Anio = forms.ChoiceField( choices=ANIOS, required=False)

    class Meta:
        model = Avaluo
        exclude = ('Salida', 'Pagado', 'Cliente', 'Depto', 'Factura', 'Prioridad')
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
                    css_class='span3'),
                Div(
                    'Edita Avaluo - Captura',
                    'Referencia',
                    'Calle',
                    'NumExt',
                    'NumInt',
                    css_class='span3'),
                Div(
                    'Colonia',
                    'Estado',
                    'Municipio',
                    'Servicio',
                    'Tipo',
                    css_class='span3'),
                css_class='row-fluid'),
            ButtonHolder(
                Submit('Buscar', 'Buscar', css_class='btn-success'),
            ))
        super(FormaConsultaSencilla,  self).__init__(*args,  **kwargs)
        self.fields['Municipio'] = forms.ModelChoiceField(required=False,  queryset=Municipio.objects.filter(estado_id__is_active='True'))


class AltaValuador(ModelForm):
    Nombre = forms.CharField()
    Apellido = forms.CharField()
    Correo = forms.CharField()

    class Meta:
        model = Valuador


class AltaUsuario(forms.Form):
  #  Form for creating new login
    Nombre = forms.CharField()
    Correo = forms.CharField()
    Usuario = forms.CharField()
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
    Factura = forms.CharField( label="")

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
                    css_class='span3'),
                css_class='row-fluid'))
        super(FacturaForm,  self).__init__(*args,  **kwargs)

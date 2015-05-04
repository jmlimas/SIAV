 # -*- coding: UTF-8 -*-
from ficha.models import *
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper, reverse
from crispy_forms.layout import *
from crispy_forms.bootstrap import *
from django.template.defaultfilters import mark_safe
from django.forms.models import formset_factory


ACTIVO = (   
    ('SI','SI'),
)

VALOR = (   
    ('Operacion','Operacion'),
    ('Mercado','Mercado'),
)


FACTOR = (
    ('0.00','-'),
    ('1.30','1.30'),
    ('1.25','1.25'),
    ('1.20','1.20'),
    ('1.15','1.15'),      
    ('1.10','1.10'),
    ('1.05','1.05'),
    ('1.00','1.00'),
    ('0.95','0.95'),
    ('0.90','0.90'),
    ('0.85','0.85'),
    ('0.80','0.80'),
    ('0.75','0.75'),
    ('0.70','0.70'),
    ('0.65','0.65'),
    ('0.60','0.60'),
)

SERVICIO_1 = (   
    ('A', 'Agua'),
    ('D', 'Drenaje'),
    ('P', 'Pavimento'),
    ('G', 'Gas'),
    ('B', 'Banquetas y Cordones'),
)

SERVICIO_2 = (    
    ('A', 'Alumbrado Público'),
    ('D', 'Drenaje Pluvial'),
    ('E', 'Energía Eléctrica'),
    ('R', 'Rec. Basura'),
    ('V', 'Vigilancia'),
)

SERVICIO_3 = (    
    ('T', 'Teléfono'),
    ('U', 'Transporte Urbano'),
    ('O', 'Otro'),
)

CONDICION = (    
    ('B', 'Condición Buena'),
    ('R', 'Condición Regular'),
    ('M', 'Condición Mala'),
)

EQUIPAMIENTO_URBANO = (  
    ('P', 'Parques y Jardínes'),
    ('I', 'Iglesias'),
    ('N', 'Nomenclatura'),
    ('M', 'Mercados'),
    ('A', 'Avenidas Principales'),
    ('O', 'Otros'),
)

USO_SUELO = (  
    ('H', 'Habitacional'),
    ('C', 'Comercial'),
    ('I', 'Industrial'),
    ('M', 'Multifamiliar'),
)

X = (  
    ('', ''),
)

SOCIOECONOMICO = (   
    ('A', 'Alto'),
    ('M', 'Medio'),
    ('B', 'Bajo'),
)

CALIDAD = (   
    ('L', 'Lujo'),
    ('B', 'Buena'),
    ('R', 'Regular'),
    ('E', 'Económica'),
    ('A', 'Autoconstrucción'),

)

NIVELES = (   
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('M', 'MÁS'),
)

URBANO_1 = (  
    ('J', 'Jardínes'),
    ('C', 'Cementerios'),
    ('A', 'Asent. Irregulares'),
)

URBANO_2 = (  
    ('Z', 'Zonas de Tolerancia'),
    ('T', 'Torres de E.E.'),
    ('O', 'Otros'),
)

RIESGO_1 = (  
    ('Z', 'Zonas de inundación'),
    ('A', 'Áreas contaminadas'),
    ('R', 'Arroyos'),
)

RIESGO_2 = (  
    ('V', 'Vados'),
    ('P', 'Pandillerismo'),
    ('O', 'Otros'),
)

USO = (
    ('HABITACIONAL','Habitacional'),
    ('COMERCIAL','Comercial'),
)
class CapturaFicha(ModelForm):
    #folio = forms.CharField(required=False, label="Folio")
    LatitudG = forms.DecimalField(required=False, label="Lon.G.")
    LatitudM = forms.DecimalField(required=False, label="Lon.M.",)
    LatitudS = forms.DecimalField(required=False, label="Lon.S.")
    LongitudG = forms.DecimalField(required=False, label="Lat.G.")
    LongitudM = forms.DecimalField(required=False, label="Lat.M.")
    LongitudS = forms.DecimalField(required=False, label="Lat.S.")
    limite_norte = forms.CharField(required=False, label = "Limite Norte")
    limite_sur = forms.CharField(required=False, label = "Limite Sur")
    limite_oriente = forms.CharField(required=False, label = "Limite Oriente")
    limite_poniente = forms.CharField(required=False, label = "Limite Poniente")
    servicio_1 = forms.MultipleChoiceField(required=False, choices=SERVICIO_1, widget=forms.CheckboxSelectMultiple, label = mark_safe('<h1><b>Servicios</b></h1>'))
    servicio_2 = forms.MultipleChoiceField(required=False, choices=SERVICIO_2, widget=forms.CheckboxSelectMultiple, label = mark_safe('<br>'))
    servicio_3 = forms.MultipleChoiceField(required=False, choices=SERVICIO_3, widget=forms.CheckboxSelectMultiple, label = mark_safe('<br>'))
    condicion = forms.MultipleChoiceField(required=False, choices=CONDICION, widget=forms.CheckboxSelectMultiple, label = mark_safe('<h1><b>Condición</b></h1>'))
    equipamiento = forms.MultipleChoiceField(required=False, choices=EQUIPAMIENTO_URBANO, widget=forms.CheckboxSelectMultiple, label = mark_safe('<h1><b>Equipamiento</b></h1>'))
    uso_suelo = forms.MultipleChoiceField(required=False, choices=USO_SUELO, widget=forms.CheckboxSelectMultiple, label = mark_safe('<h1><b>Uso Suelo</b></h1>'))
    socioeconomico = forms.MultipleChoiceField(required=False, choices=SOCIOECONOMICO, widget=forms.CheckboxSelectMultiple, label = mark_safe('<h1><b>Socioeconómico</b></h1>'))
    calidad = forms.MultipleChoiceField(required=False, choices=CALIDAD, widget=forms.CheckboxSelectMultiple, label = mark_safe('<h1><b>Calidad</b></h1>'))
    niveles = forms.MultipleChoiceField(required=False, choices=NIVELES, widget=forms.CheckboxSelectMultiple, label = mark_safe('<h1><b>Niveles</b></h1>'))
    entorno_urbano_1 = forms.MultipleChoiceField(required=False, choices=URBANO_1, widget=forms.CheckboxSelectMultiple, label = mark_safe('<h1><b>Entorno Urbano</b></h1>'))
    entorno_urbano_2 = forms.MultipleChoiceField(required=False, choices=URBANO_2, widget=forms.CheckboxSelectMultiple, label = mark_safe('<br>'))
    riesgo_1 = forms.MultipleChoiceField(required=False, choices=RIESGO_1, widget=forms.CheckboxSelectMultiple, label = mark_safe('<h1 ><b>Factores Riesgo</b></h1>'))
    riesgo_2 = forms.MultipleChoiceField(required=False, choices=RIESGO_2, widget=forms.CheckboxSelectMultiple, label = mark_safe('<br>'))
    densidad = forms.CharField(required=False, label = mark_safe('<h1  style="text-align:left"><b>Densidad</b></h1>'))
    observaciones = forms.CharField(required=False, widget=forms.Textarea, label = "Observaciones")
    class Meta:
        model = Ficha_Tecnica
        fields = ('LatitudG','LatitudM','LatitudS','LongitudG','LongitudM','LongitudS','limite_norte','limite_sur','limite_oriente','limite_poniente','servicio_1','servicio_2','servicio_3','condicion','equipamiento','uso_suelo',
                    'socioeconomico','calidad','niveles','entorno_urbano_1','entorno_urbano_2','riesgo_1','riesgo_2','densidad','observaciones')
    def __init__(self,  *args,  **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-CapturaFicha'
        self.helper.form_class = 'blueForms'
        self.helper.form_tag = False
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Div(
                    HTML("<div class='control-group' style='visibility: hidden;'><label class='control-label'>Promedio:</label><input type='text' class='input-medium textinput textInput'></input></div>"),
                    HTML("<div class='control-group' style='visibility: hidden;'><label class='control-label'>Promedio:</label><input type='text' class='input-medium textinput textInput'></input></div>"),

                	#'folio',
                    Field('limite_norte',css_class='input-medium'),
                    'servicio_1',
                    HTML("<br>"),
                    'uso_suelo',
                    HTML("<br>"),
                    InlineCheckboxes('socioeconomico'),
                    HTML("<br>"), 
                    'entorno_urbano_1',
                    HTML("<br>"),
                    'observaciones',    
                    css_class='span3'),
                Div(
                    Field('LatitudG',  css_class='input-medium'),  
                    Field('LongitudG',  css_class='input-medium'),  
                    Field('limite_sur',css_class='input-medium'),
                    'servicio_2',
                    HTML("<br>"),
                    'calidad',
                    HTML("<br>"),
                    HTML("<br>"),
                    HTML("<br>"),
                    HTML("<br>"),  
                    'entorno_urbano_2',
                    HTML("<br>"), 
                    HTML("<br>"),             
                    css_class='span3'),
                Div(
                     Field('LatitudM',  css_class='input-medium'),  
                     Field('LongitudM',  css_class='input-medium'), 
                     Field('limite_oriente',css_class='input-medium'),
                     'servicio_3',
                     HTML("<br>"),
                     HTML("<br>"),
                     'condicion',
                     HTML("<br>"),
                     HTML("<br>"),
                     InlineCheckboxes('niveles'),
                     HTML("<br>"),
                     'riesgo_1',          
                    css_class='span3'),
                Div(
                     Field('LatitudS',  css_class='input-medium'), 
                     Field('LongitudS',  css_class='input-medium'), 
                     Field('limite_poniente',css_class='input-medium'),
                     'equipamiento',
                     HTML("<br>"),
                     HTML("<br>"),
                     AppendedText('densidad', '%', active=True),
                     HTML("<br>"),
                     HTML("<br>"),
                     HTML("<br>"),
                     'riesgo_2',

                    css_class='span3'),css_class='row-fluid'),
            #'Algo',
           # ButtonHolder(
           #     Submit('submit',  'Enviar',  css_class='btn-success btn-large'))
            )
        super(CapturaFicha,  self).__init__(*args,  **kwargs)

class SimpleCapturaFicha(ModelForm):
    #folio = forms.CharField(required=False, label="Folio")
    limite_norte = forms.CharField(required=False, label = "Limite Norte")
    limite_sur = forms.CharField(required=False, label = "Limite Sur")
    limite_oriente = forms.CharField(required=False, label = "Limite Oriente")
    limite_poniente = forms.CharField(required=False, label = "Limite Poniente")
    servicio_1 = forms.MultipleChoiceField(required=False, choices=SERVICIO_1, widget=forms.CheckboxSelectMultiple, label = mark_safe('<h1><b>Servicios</b></h1>'))
    servicio_2 = forms.MultipleChoiceField(required=False, choices=SERVICIO_2, widget=forms.CheckboxSelectMultiple, label = mark_safe('<br>'))
    servicio_3 = forms.MultipleChoiceField(required=False, choices=SERVICIO_3, widget=forms.CheckboxSelectMultiple, label = mark_safe('<br>'))
    condicion = forms.MultipleChoiceField(required=False, choices=CONDICION, widget=forms.CheckboxSelectMultiple, label = mark_safe('<h1><b>Condición</b></h1>'))
    equipamiento = forms.MultipleChoiceField(required=False, choices=EQUIPAMIENTO_URBANO, widget=forms.CheckboxSelectMultiple, label = mark_safe('<h1><b>Equipamiento</b></h1>'))
    uso_suelo = forms.MultipleChoiceField(required=False, choices=USO_SUELO, widget=forms.CheckboxSelectMultiple, label = mark_safe('<h1><b>Uso Suelo</b></h1>'))
    socioeconomico = forms.MultipleChoiceField(required=False, choices=SOCIOECONOMICO, widget=forms.CheckboxSelectMultiple, label = mark_safe('<h1><b>Socioeconómico</b></h1>'))
    calidad = forms.MultipleChoiceField(required=False, choices=CALIDAD, widget=forms.CheckboxSelectMultiple, label = mark_safe('<h1><b>Calidad</b></h1>'))
    niveles = forms.MultipleChoiceField(required=False, choices=NIVELES, widget=forms.CheckboxSelectMultiple, label = mark_safe('<h1><b>Niveles</b></h1>'))
    entorno_urbano_1 = forms.MultipleChoiceField(required=False, choices=URBANO_1, widget=forms.CheckboxSelectMultiple, label = mark_safe('<h1><b>Entorno Urbano</b></h1>'))
    entorno_urbano_2 = forms.MultipleChoiceField(required=False, choices=URBANO_2, widget=forms.CheckboxSelectMultiple, label = mark_safe('<br>'))
    riesgo_1 = forms.MultipleChoiceField(required=False, choices=RIESGO_1, widget=forms.CheckboxSelectMultiple, label = mark_safe('<h1 ><b>Factores Riesgo</b></h1>'))
    riesgo_2 = forms.MultipleChoiceField(required=False, choices=RIESGO_2, widget=forms.CheckboxSelectMultiple, label = mark_safe('<br>'))
    densidad = forms.CharField(required=False, label = mark_safe('<h1  style="text-align:left"><b>Densidad</b></h1>'))
    observaciones = forms.CharField(required=False, widget=forms.Textarea, label = "Observaciones")

class InvestigacionMercado(ModelForm):
    investigacion_id = forms.CharField(required=False, label = "Calle")
    calle = forms.CharField(required=False, label = "Domicilio")
    #colonia = forms.CharField(required=False, label = "Colonia")
    fuente = forms.CharField(required=False, label = "Fuente")
    telefono = forms.CharField(required=False, label = "Telefono")
    uso = forms.ChoiceField( choices=USO, required=False)
    m_terreno = forms.DecimalField (required=False, label = "Mts. Terreno")
    m_construccion = forms.DecimalField (required=False, label = "Mts. Construccion")
    oferta = forms.DecimalField (required=False, label = "Oferta")
    unitario_0 = forms.DecimalField (required=False, label = "Unitario")
    unitario = forms.DecimalField (required=False, label = "Unitario Terreno")
    factor = forms.ChoiceField( choices=FACTOR, required=False)
    class Meta:
        model = Investigacion_Mercado
        fields = ('calle','fuente','telefono','uso','m_terreno','m_construccion','oferta','unitario_0','unitario','investigacion_id','factor')
    def __init__(self,  *args,  **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-InvestigacionMercado'
        self.helper.form_class = 'blueForms'
        self.helper.form_tag = False
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div(
                        Div(Field('calle',  css_class='span20 input-large'),  css_class='span2'),
                        Div(Field('fuente',  css_class='span16 input-medium'),  css_class='span2'),
                        Div(Field('telefono',  css_class='span16 input-medium'),  css_class='span2'),
                        Div(Field('uso',  css_class='span16 input-medium'),  css_class='span2'),
                        Div(PrependedText('oferta', '$', active=True,css_class='input-medium span12'), css_class='span2')),
                    css_class='span12'),
                Div(
                    Div(
                        Div(Field('m_terreno',  css_class='span20 input-large'),  css_class='span2'),
                        Div(Field('m_construccion',  css_class='span16 input-medium'),  css_class='span2')),
                         
                    css_class='span12 '),
                Div(
                    Div(
                        Div(Field('unitario_0',  css_class='span16 input-medium'),  css_class='span2'),
                        Div(HTML("""<h3 style="padding-top:8px;padding-right:8px">X</h3>"""),  css_class='span1'),
                        Div(Field('factor',  css_class='span20 input-large'),  css_class='span1'), 
                        Div(HTML("""<h3 style="padding-top:8px;padding-right:8px">=</h3>"""),  css_class='span1'),
                        Div(Field(AppendedPrependedText('unitario', '$','/m²', active=True,css_class='input-small unitario')))),
                    css_class='span12 '),
                css_class='row-fluid'),
            #'Algo',
            #ButtonHolder(
            #    Submit('submit',  'Enviar',  css_class='btn-success btn-large'))
            )
        super(InvestigacionMercado,  self).__init__(*args,  **kwargs)



class ValorPropuesto(ModelForm):
  
    valor_propuesto = forms.DecimalField (required=False, label = "Valor Propuesto")
    factor = forms.ChoiceField( choices=FACTOR, required=False)

    class Meta:
        model = Ficha_Tecnica
        fields = ('valor_propuesto','factor')
    def __init__(self,  *args,  **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-ValorPropuesto'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Div(
                    HTML("<div class='control-group' style='visibility: visible;'><label class='control-label'>Promedio:</label><input type='text' id='id_Promedio' class='input-medium textinput textInput'></input></div>"),
                    css_class='span2'),
                 Div(
                    HTML("""<h3 style="padding-top:8px;padding-top:8px">X</h3>"""),  
                    css_class='span1'),
                Div(
                    Field('factor',  css_class='span16 input-medium'),  
                    css_class='span2'),
                Div(
                    HTML("""<h3 style="padding-top:8px">=</h3>"""),  
                    css_class='span2'),
                Div(
                    AppendedPrependedText('valor_propuesto', '$','/m²', active=True,css_class='input-large'),
                        css_class='span5'),
                 css_class='row-fluid'),
            #'Algo',
            #ButtonHolder(
            #    Submit('submit',  'Enviar',  css_class='btn-success btn-large'))
            )
        super(ValorPropuesto,  self).__init__(*args,  **kwargs)


class ValoresUnitarios(ModelForm):
    valores_id = forms.CharField(required=False, label = "Calle")
    valores_id = forms.CharField(required=False, label = "Activo")
    valor_operacion = forms.DecimalField (required=False, label = "Valor Operacion")
    valor_mercado = forms.DecimalField (required=False, label = "Valor Mercado")
    activo = forms.ChoiceField( choices=USO, required=False)


    class Meta:
        model = Valores_Unitarios
        fields = ('valor_operacion','valor_mercado','valores_id','activo')
    def __init__(self,  *args,  **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-ValoresUnitarios'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Div(
                    Field(AppendedPrependedText('valor_operacion', '$','/m²', active=True,css_class='input-small valor_operacion')),
                    css_class='span3'),
                Div(
                    Field(AppendedPrependedText('valor_mercado', '$','/m²', active=True,css_class='input-small valor_mercado')),
                    Hidden('activo','SI'),
                    css_class='span2'),
                 css_class='row-fluid offset3'),
            #'Algo',
            #ButtonHolder(
            #    Submit('submit',  'Enviar',  css_class='btn-success btn-large'))
            )
        super(ValoresUnitarios,  self).__init__(*args,  **kwargs)

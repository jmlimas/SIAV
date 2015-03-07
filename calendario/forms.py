from calendario.models import Evento
from django.forms import ModelForm,fields, models, formsets, widgets

class VisitadorForm(ModelForm):
    Visitador = forms.CharField(label="Visitador",required=True,queyset=User.objects.filter(groups__name='Visitador'))

    class Meta:
        model = Evento
        fields = ('Visitador')

    def __init__(self,  *args,  **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-VisitadorForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'POST'
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(Div('Factura',
                    css_class='col-md-3'),
                css_class='row'))
        super(FacturaForm,  self).__init__(*args,  **kwargs)

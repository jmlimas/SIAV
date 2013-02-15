from app.models import Estado

from django import template

register = template.Library()

@register.inclusion_tag("selecciona_estado.html")
def selecciona_estado():
    lista_estados = Estado.objects.all()
    return {'lista_estados' : lista_estados}

from django import template
register = template.Library()

import calendar

@register.filter
def month_name(x):
    return {
        1: 'Enero',
        2: 'Febrero',
        3: 'Marzo',
        4: 'Abril',
        5: 'Mayo',
        6: 'Junio',
        7: 'Julio',
        8: 'Agosto',
        9: 'Septiembre',
        10: 'Octubre',
        11: 'Noviembre',
        12: 'Diciembre',
        0: 'N/D'
        }.get(x, "N/D")    # 9 is default if x not found

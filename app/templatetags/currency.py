from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()

def currency(dollars):
    if dollars:
        dollars = round(float(str(dollars)), 2)
        return "$%s%s" % (intcomma(int(dollars)), ("%0.2f" % dollars)[-3:])
    else:
        return 0

register.filter('currency', currency)

from django import template
import numbers

register = template.Library()

def adder(avaluo):
	total_general = 0.0
    #if avaluo is None:
    #    return '0'
 	for a in avaluo:
 		if a.Importe:
 			if isinstance(a.Importe, numbers.Real):  
 				total_general += float(str(a.Importe))
 	return total_general


def importe_adder(avaluo):
	total_general = 0.0
    #if avaluo is None:
    #    return '0'
 	for a in avaluo:
 		if isinstance(a['total'], numbers.Real):  
 			total_general += float(str(a['total']))
 	return total_general



register.filter('adder', adder)
register.filter('importe_adder', importe_adder)
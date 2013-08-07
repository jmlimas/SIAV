from django import template

register = template.Library()

def adder(avaluo):
	total_general = 0.0
    #if avaluo is None:
    #    return '0'
 	for a in avaluo:
 		if a.Importe:
 			total_general += float(str(a.Importe))
 	return total_general

register.filter('adder', adder)

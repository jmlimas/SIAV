from django import template
import ast

register = template.Library()

def dic_length(value):
	if value:
		value = [ item.encode('ascii') for item in ast.literal_eval(value) ]
		return len(value)
	else:
		return 0

register.filter('dic_length', dic_length)
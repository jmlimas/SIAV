from django import template

register = template.Library()

def dic_length(value):
	if value is None:
		return 0
	else:
		return len(value)

register.filter('dic_length', dic_length)
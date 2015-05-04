from django import template
import math

register = template.Library()

def round_hunded(value):

	def roundup(x):
		return int(round(float(x) / 100.00)) * 100.00
	if value:
		value = roundup(value)
		return value
	else:
		return 0

def round_hunded_10(value):

	def roundup(x):
		return int(round(float(x) / 10.00)) * 10.00
	if value:
		value = roundup(value)
		return value
	else:
		return 0

register.filter('round_hunded', round_hunded)
register.filter('round_hunded_10', round_hunded_10)
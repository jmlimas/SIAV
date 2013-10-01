from django import template
import os.path

register = template.Library()

def file_exists(url):
	return os.path.exists(url)
	
register.filter('file_exists', file_exists)

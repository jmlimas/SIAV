from django import template
import os.path
from settings import *
import urllib

register = template.Library()

def file_exists(url):
	url = urllib.unquote(url)
	return os.path.exists(url)
	
register.filter('file_exists', file_exists)

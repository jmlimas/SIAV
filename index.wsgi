import os
import sys
import site

# Add the app's directory to the PYTHONPATH
sys.path.append('/home/SIAV')

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

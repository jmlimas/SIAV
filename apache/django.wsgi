import os
import sys

path = '/var/www/purpleblue_com'
if path not in sys.path:
    sys.path.insert(0, '/var/www/SIAV')

os.environ['DJANGO_SETTINGS_MODULE'] = 'SIAV.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

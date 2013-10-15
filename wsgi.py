import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SIAV.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program command options
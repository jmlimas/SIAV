import newrelic.agent

newrelic.agent.initialize('./newrelic.ini')

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SIAV.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
application = newrelic.agent.wsgi_application()(application)
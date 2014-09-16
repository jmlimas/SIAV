import newrelic.agent
import os
from django.core.wsgi import get_wsgi_application

newrelic.agent.initialize('./newrelic.ini')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

application = get_wsgi_application()

application = newrelic.agent.wsgi_application()(application)

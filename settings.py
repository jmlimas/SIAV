# Django settings for SIAV project.

import os
import django 

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "SIAV.settings"

CRISPY_TEMPLATE_PACK = 'bootstrap3'

#def show_toolbar(request):
#    return True
#SHOW_TOOLBAR_CALLBACK = show_toolbar

#INTERNAL_IPS = ('127.0.0.1',)
#DEBUG_TOOLBAR_PATCH_SETTINGS = False

ALLOWED_HOSTS = ['*']
DEBUG = True
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = True 
THUMBNAIL_PREFIX ='media/cache/'

DEFAULT_CHARSET = 'utf-8' 
FILE_CHARSET = 'utf-8' 

include_resource_uri = False

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'siavdb',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'siavdb',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default.
        'OPTIONS': {"init_command": "SET foreign_key_checks = 0;"}
    }
}


ROOT_URLCONF = '/SIAV/'

# URL of the login page.
LOGIN_URL = '/SIAV/login/'

# URL of the logout page.
LOGOUT_URL = '/SIAV/logout/'

# URL to redirect after login
LOGIN_REDIRECT_URL = '/SIAV/captura/'


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Monterrey'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-MX'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

USE_THOUSAND_SEPARATOR = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = False

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.dirname("media")
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = os.path.dirname("media")

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = 'C:/inetpub/wwwroot/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
#STATIC_URL = 'http://valnorte.net:100/'
#STATIC_URL = 'http://localhost:100/'
# Url para desarrollo
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #'C:/inetpub/wwwroot/SIAV/app/static'
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'dajaxice.finders.DajaxiceFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'qkzzj4+7+_4uimqr(f4lhjv1u=^_qbky$qnnnfi7*@$&amp;a-8jzx'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    #'django_pdb.middleware.PdbMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'SIAV.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    "templates",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'app',
    'websock',
    'endless_pagination',
    'example_project',
    'south',
    'crispy_forms',
    #'django_socketio',
    #'debug_toolbar',
    'grappelli',
    'sorl.thumbnail',
    'tastypie',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'bootstrap3',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    "django.core.context_processors.request",
    'django.contrib.messages.context_processors.messages',
)




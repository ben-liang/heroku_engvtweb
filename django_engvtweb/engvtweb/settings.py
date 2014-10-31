"""
Django settings for project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
from django_engvtweb import repository_path
from urlparse import urlparse

## Hack here to get environment variables from .env
## source: https://gist.github.com/vlasovskikh/e8fe8e0a5c4a73048a09
from subprocess import Popen, PIPE
import pickle
PYTHON_DUMP_ENVIRON = """\
import sys
import os
import pickle

data = pickle.dumps(os.environ)
stdout = os.fdopen(sys.stdout.fileno(), "wb")
stdout.write(data)
"""

def source_bash_file(path):
    bash_cmds = [
        "source '%s'" % path,
        "python -c '%s'" % PYTHON_DUMP_ENVIRON,
    ]
    p = Popen(['bash', '-c', '&&'.join(bash_cmds)], stdout=PIPE)
    stdout, _ = p.communicate()
    if stdout:
        environ = pickle.loads(stdout)
        for k, v in environ.items():
            os.environ[k] = v

REPOSITORY_PATH = repository_path()
#now source DATABASE_URL var from .env file
source_bash_file(os.path.join(REPOSITORY_PATH, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
DEFAULT_SECRET_KEY = '3iy-!-d$!pc_ll$#$elg&cpr@*tfn-d5&n9ag=)%#()t$$5%5^'
SECRET_KEY = os.environ.get('SECRET_KEY', DEFAULT_SECRET_KEY)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

#Custom Path handling
DJANGO_IMPORT_ROOT = 'django_engvtweb'
def _engvtimport(*import_path):
    """Fully qualified import path relative to :data:`DJANGO_IMPORT_ROOT`

    :param list import_path: one or more levels underneath the root

    :returns: fully qualified import path
    :rtype: str
    """

    return '.'.join([DJANGO_IMPORT_ROOT] + list(import_path))

# Application definition
INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'bootstrap3',
    'changuito',
    'haystack',
) + tuple(map(_engvtimport, [
    'team_order',
    'engvtweb',
    'cart',
]))


#Heroku SearchBox (ElasticSearch add-on) configuration
es = urlparse(os.environ.get('SEARCHBOX_URL') or 'http://127.0.0.1:9200/')
port = es.port or 80

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': es.scheme + '://' + es.hostname + ':' + str(port),
        'INDEX_NAME': 'documents',
        'INCLUDE_SPELLING': True,
    },
}
if es.username:
    HAYSTACK_CONNECTIONS['default']['KWARGS'] = {"http_auth": es.username + ':' + es.password}


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'changuito.middleware.CartMiddleware',
)

ROOT_URLCONF = _engvtimport('engvtweb.urls')

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Parse database configuration from $DATABASE_URL
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(REPOSITORY_PATH, 'templates'),
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

STATICFILES_DIRS = (
    os.path.join(REPOSITORY_PATH, 'static'),
)

GRAPPELLI_ADMIN_TITLE = 'ENGVTWeb'
# imports
import os
from root.constants import Environment
from .base import *  # pylint: disable=wildcard-import, unused-wildcard-import

# End: imports -----------------------------------------------------

ALLOWED_HOSTS = [os.environ['DOMAIN']]

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = os.environ.get('DEBUG') == 'True'

# Ensure correct ENV
ENV = Environment.PROD

# Security
X_FRAME_OPTIONS = 'SAMEORIGIN'
CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = 0
SECURE_SSL_REDIRECT = False
SECURE_HSTS_PRELOAD = False
SESSION_COOKIE_SECURE = False
SECURE_BROWSER_XSS_FILTER = False
SECURE_CONTENT_TYPE_NOSNIFF = False
SECURE_HSTS_INCLUDE_SUBDOMAINS = False

DATABASES = {
    'default':
        {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['DB_NAME'],
            'USER': os.environ['DB_USER'],
            'PASSWORD': os.environ['DB_PASSWORD'],
            'HOST': os.environ['DB_HOST'],
            'PORT': os.environ['DB_PORT'],
        }
}

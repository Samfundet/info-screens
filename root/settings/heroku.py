# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
import os
import django_heroku
from .base import *

ALLOWED_HOSTS = ['info-screens.herokuapp.com']

# Values are set in heroku dashboard
SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = os.environ['DEBUG'] == True

# pylint: disable=undefined-variable
# Ensure correct ENV
ENV = Environment.HEROKU

#  Add configuration for static files storage using whitenoise, heroku
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',  # whitenoise, heroku
]

# activate django-heroku.
django_heroku.settings(locals())

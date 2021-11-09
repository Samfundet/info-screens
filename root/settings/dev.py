# pylint: disable=unused-wildcard-import
import os

from ..constants import Environment
from .base import *  # pylint: disable=wildcard-import

ALLOWED_HOSTS = ['*']

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = True

# Ensure correct ENV
ENV = Environment.DEV

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

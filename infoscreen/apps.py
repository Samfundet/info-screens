from django.apps import AppConfig
from django.core import management


class InfoScreenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'infoscreen'

    def ready(self):
        try:
            # https://docs.djangoproject.com/en/3.0/ref/django-admin/#createsuperuser
            management.call_command('createsuperuser', interactive=False)
        except management.CommandError:
            pass

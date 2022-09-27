from django.apps import AppConfig
from django.core import management


class InfoScreenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'infoscreen'

    def ready(self):
<<<<<<< HEAD
        try:
            # https://docs.djangoproject.com/en/3.0/ref/django-admin/#createsuperuser
            management.call_command('createsuperuser', interactive=False)
        except management.CommandError:
=======

        from django.core import management

        try:
            # https://docs.djangoproject.com/en/3.0/ref/django-admin/#createsuperuser
            management.call_command('createsuperuser', interactive=False)
        except:
>>>>>>> 035aec60c9b1249ca1761f39c5fdafbc26602740
            pass

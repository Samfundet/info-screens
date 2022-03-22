# imports
from django import template
from django.conf import settings

# End: imports -----------------------------------------------------------------

register = template.Library()

# https://docs.djangoproject.com/en/3.0/howto/custom-template-tags/


@register.inclusion_tag("infoscreen/components/screen.html")
def screen_component(screen, *args, **kwargs):
    default_classes = ""
    return {
        "screen": screen,
        "classes": kwargs.get("classes", default_classes),
    }


@register.inclusion_tag("infoscreen/components/navbar.html")
def navbar_component(*args, **kwargs):
    default_classes = ""
    return {
        "classes": kwargs.get("classes", default_classes),
    }

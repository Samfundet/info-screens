from django.contrib import admin

from infoscreen import models as infoscreen_models
from root import models as root_models


class ScreenAdmin(root_models.CustomBaseAdmin):
    list_display = ['name']
    ordering = []
    # list_filter = []
    filter_horizontal = ['images']
    search_fields = ['name']
    
    
class ScreenHasImageAdmin(admin.ModelAdmin):
    list_display = ['screen', 'image', 'nr']
    ordering = ['screen', 'nr']
    list_filter = ['screen', 'image']
    # filter_horizontal = []
    search_fields = ['screen__name', 'image__name']


class ImageAdmin(root_models.CustomBaseAdmin):
    list_display = ['name', 'url']
    ordering = ['name']
    # list_filter = []
    # filter_horizontal = []
    search_fields = ['name']


admin.site.register(infoscreen_models.Screen, ScreenAdmin)
# admin.site.register(infoscreen_models.ScreenHasImage, ScreenHasImageAdmin)
admin.site.register(infoscreen_models.Image, ImageAdmin)
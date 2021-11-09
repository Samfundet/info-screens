from django.views import View
from django.shortcuts import render, get_object_or_404

from infoscreen import models as infoscreen_models


class Index(View):
    template = 'infoscreen/index.html'

    def get(self, request):
        return render(request, self.template)


class ScreenView(View):
    template = 'infoscreen/screen.html'

    def get(self, request, slug):
        screen = get_object_or_404(infoscreen_models.Screen, slug=slug)
        return render(request, self.template, {
            'screen': screen,
        })


class ScreenListView(View):
    template = 'infoscreen/screen_list.html'

    def get(self, request):
        screens = infoscreen_models.Screen.objects.all()
        return render(request, self.template, {
            'screens': screens,
        })

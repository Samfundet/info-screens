from django.urls import path
from django.views.generic.base import RedirectView

from infoscreen import views

app_name = 'infoscreen'

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='infoscreen:screen_list'), name='index'),
    path('screen/<str:slug>/', views.ScreenView.as_view(), name='view_screen'),
    path('screens/', views.ScreenListView.as_view(), name='screen_list'),
]

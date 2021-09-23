from django.urls import path, include
from infoscreen import views

app_name = 'infoscreen'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('screen/<str:slug>/', views.ScreenView.as_view(), name='screen'),
]


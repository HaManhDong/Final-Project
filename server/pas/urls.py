from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('devices-info/', views.devices_info, name='devices-info'),
]
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('devices-info/', views.devices_info, name='devices-info'),
    path('users-info/', views.users_info, name='users-info'),
    path('api/users/', views.users_api, name='api/users'),
]
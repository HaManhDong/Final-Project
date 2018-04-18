from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('devices-info/', views.devices_info, name='devices-info'),
    path('warning/', views.warning, name='warning'),
    path('members-info/', views.members_info, name='members-info'),
    re_path(r'^member-profile/', views.member_profile, name='member-profile'),
    re_path(r'^member/train/', views.train_face),
    path('api/members/', views.members_api, name='api/members'),
    path('api/server-auth/', views.server_authentication, name='api/server-auth'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
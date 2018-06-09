from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views, apis

urlpatterns = [
    path('', views.index, name='index'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('devices-info/', views.devices_info, name='devices-info'),
    path('warning/', views.warning, name='warning'),
    path('members-info/', views.members_info, name='members-info'),
    re_path(r'^member-profile/', views.member_profile, name='member-profile'),
    re_path(r'^member/train/', views.train_face),
    path('api/member/', views.member_api, name='api/member'),
    path('api/change-card-id/', views.change_card_id, name='api/change-card-id'),
    path('api/upload_video/', views.upload_video, name='api/upload_video'),
    path('api/server-auth/', views.server_authentication, name='api/server-auth'),
    path('calculate_hour/', apis.calculate_hour, name='calculate_hour'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),

    path('test/', apis.test),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
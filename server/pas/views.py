import os

from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.core.files.images import ImageFile
from django.core.files.storage import default_storage
from django.conf import settings

from .models import User


def index(request):
    return render(request, 'pas/index.html')


def devices_info(request):
    return render(request, 'pas/devices.html')


def users_info(request):
    try:
        user_list = User.objects.all()
        context = {
            'user_list': user_list,
        }
    except User.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'pas/users.html', context)


def users_api(request):
    try:
        user_list = User.objects.all()
    except User.DoesNotExist:
        raise Http404("Question does not exist")
    return HttpResponse(user_list)


def upload_images(request):
    if request.method == 'POST':
        data = request.FILES['face']
        face = ImageFile(data)
        path = default_storage.save('tmp/' + str(data), face)
        os.path.join(settings.BASE_DIR, path)
        return HttpResponse("POST request success")
    return HttpResponse("Upload image success")

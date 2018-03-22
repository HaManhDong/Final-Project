from django.http import Http404, HttpResponse
from django.shortcuts import render

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
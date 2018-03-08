from django.http import Http404
from django.shortcuts import render

from .models import User


def index(request):
    try:
        user_list = User.objects.all()
        context = {
            'user_list': user_list,
        }
    except User.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'pas/index.html', context)

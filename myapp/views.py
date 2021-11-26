from urllib import request

from django.shortcuts import render
from .logic import get_objects


def objects_list(request):
    obj = get_objects()
    return render(request, 'index.html', context={'name': obj, 'image': obj})

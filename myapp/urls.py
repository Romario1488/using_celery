from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', objects_list, name='objects_list_url'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

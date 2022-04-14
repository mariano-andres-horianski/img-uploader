from unicodedata import name
from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

app_name = 'uploader_page'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload', views.image_upload_view, name='upload'),
]
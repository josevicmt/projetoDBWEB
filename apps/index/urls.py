from django.urls import path
from django.urls.conf import include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('verPost/<int:pk>/<str:slug>', verPost, name='verPost'),
]

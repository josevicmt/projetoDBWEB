from django.urls import path
from django.urls.conf import include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('verPost/<int:pk>/<str:slug>', verPost, name='verPost'),
    path('verPost/<int:pk>/<str:slug>/excluir', excluirPost, name='excluirPost'),
    path('verPost/<int:pk>/<str:slug>/editar', editarPost, name='editarPost'),


]

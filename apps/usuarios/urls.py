from django.contrib.auth import logout
from django.urls import path
from .views import loginView, registro


urlpatterns = [
    path('', loginView, name='login_view'),
    path('cadastro', registro, name='registro_view'),
    path('logout', logout, name='logout')

]


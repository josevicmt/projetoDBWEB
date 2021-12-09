from django.contrib.auth import logout
from django.urls import path
from .views import loginView, registro
from django.contrib.auth.views import LogoutView
from django.conf import settings



urlpatterns = [
    path('', loginView, name='login_view'),
    path('cadastro', registro, name='registro_view'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout')

]


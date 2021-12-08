from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout

from .forms import LoginForm, UsuariosCria
# Create your views here.

User = get_user_model()

def logout_view(request):
    logout(request)
    return redirect('/')

def loginView(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        nome_usuario= form.cleaned_data.get('username')
        senha= form.cleaned_data.get('password')
        user= authenticate(username=nome_usuario, password=senha)
        login(request, user)

        return redirect('/dashboard')        

    contexto={
        'form': form
    }
    return render(request, 'index.html', contexto)

def registro(request):
    """Segunda Página, apenas cadastro de usuário"""
    form_registro= UsuariosCria(request.POST or None)
    #print(request.POST or None)
    if form_registro.is_valid():
        email= form_registro.cleaned_data.get('email')
        username= form_registro.cleaned_data.get('username')
        nome= form_registro.cleaned_data.get('nome_completo')
        senha2= form_registro.cleaned_data.get('password2')

        usuario=User.objects.create_user(username=username, email=email, nome_completo=nome, password=senha2)
        usuario.save()

    context={
        'form': form_registro,
    }
    return render(request,'cadastro.html', context)
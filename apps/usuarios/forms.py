from django import forms
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.core.validators import EmailValidator
#from django.forms import widgets
from .validators import *

class UsuariosCria(forms.ModelForm):
    password1= forms.CharField(label='Password', widget=forms.PasswordInput)
    password2= forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model= CustomUsuario
        verbose_name = 'CustomUsuario'
        verbose_name_plural = 'Usuarios Customizados'
        fields=[
            'email',
            'nome_completo',
            'username',
        ]
        labels={
            'email':'',
            'nome_completo':'',
            'username':'',
            'password1':'',
            'password2':'',
        }

        widgets={
            'email':forms.EmailInput(attrs={'type':'text', 'class':'form-control form-control-xl', 'placeholder':'Email'}),
            'nome_completo':forms.TextInput(attrs={'placeholder':'Nome completo', 'class':'form-control form-control-xl'}),
            'username': forms.TextInput(attrs={'placeholder':'Username', 'class':'form-control form-control-xl'}),
            'password1':forms.Textarea(attrs={'placeholder':'Confirme a Senha', 'class':'form-control form-control-xl'}),
            'password2':forms.Textarea(attrs={'placeholder':'Confirme a Senha','type':'password', 'class':'form-control form-control-xl'}),
        }

    def clean(self):
        password1= self.cleaned_data.get('password1')
        password2= self.cleaned_data.get('password2')
        if str(password1) == str(password2):
            return self.cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
        "class": "form-control"
    }))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password"
            }
        )
    )
    def clean(self):
        username= self.cleaned_data.get('username')
        password= self.cleaned_data.get('password')
        if username and password:
            user= authenticate(username=username, password= password)
            if user is None:
                raise forms.ValidationError('Esse usuário não existe')
            if not user.check_password(password):
                raise forms.ValidationError('Senha inválida')
            if not user.is_active:
                raise forms.ValidationError('Usuário não autorizado')
        else:
            raise forms.ValidationError('Insira login e senha válidos')
        return self.cleaned_data
    
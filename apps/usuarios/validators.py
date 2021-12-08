from django.core.exceptions import ValidationError
from .models import CustomUsuario

def numero_string(palavra, campo, lista):    
    if not palavra:
        lista[campo]='Nome inválido'
        return
    if any(char.isdigit() for char in palavra):
        lista[campo]= 'Insira um nome válido, sem digitos'

def checa_senhas(senha1, senha2, campo, lista):
    if not (senha1 and senha2):
        lista[campo]='Semnhas inválidas'
        return
    if senha1 != senha2:
        lista[campo]= 'Insira senhas iguais'

def nome_db(nome_usuario, campo, lista):
    user= CustomUsuario.objects.all()
    nomes= []
    if not nome_usuario:
        lista[campo]='Nome inválido'
        return
    for usuario in user:
        nomes+= [usuario.username]
    if nome_usuario in nomes:
        lista[campo]='Nome de usuário Inválido'

def email_db(email, campo, lista):
    user= CustomUsuario.objects.all()
    emails= []
    if not email:
        lista[campo]='Email inválido'
        return
    for usuario in user:
        emails+= [usuario.email]
    if email in emails:
        lista[campo]='Email já cadastrado, deseja recuperar a senha?'
        return


    allow_list=['gmail', 'outlook', 'yahoo', 'hotmail', 'eject', 'edu', 'ect', 'ufrn']
    
    bloqueado= True
    for dominio in allow_list:
        if dominio in email:
            bloqueado= False
    if bloqueado:
        lista[campo]='Email inválido'
        return
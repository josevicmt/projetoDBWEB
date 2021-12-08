from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUsuario(AbstractUser):
    email= models.EmailField('Email', unique=True)
    nome_completo= models.CharField('Nome Completo', max_length=360, unique=True)
    username= models.CharField('Username', max_length=50, unique=True)
    password= models.CharField('Password', max_length=150)
    imagem= models.ImageField('Imagem de Usuario', upload_to='media/user/profile.', null=True, blank=True)
    is_active= models.BooleanField(default=True)
    is_admin= models.BooleanField(default=False)

    USERNAME_FIELD='username'
    REQUIRED_FIELDS=[]

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True 

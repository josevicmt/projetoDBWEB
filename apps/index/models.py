from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model as user

User = user()

class Post(models.Model):
    usuario  = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    titulo   = models.CharField('Titulo', blank=False, max_length=150, unique=True)
    anotacao = models.TextField('Anotacao')
    criacao  = models.DateTimeField(auto_now=True)
    edicao   = models.DateTimeField(auto_now_add=True)
    slug     = models.SlugField(default='', editable=False)   
    class Meta:
        ordering=['-criacao', '-titulo']
    
    def get_vizualizacao_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug,
        }
        return reverse('verPost', kwargs=kwargs)
    
    def get_excluir_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug,
        }
        return reverse('excluirPost', kwargs=kwargs)
    
    def get_editar_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug,
        }
        return reverse('editarPost', kwargs=kwargs)
    
    def verMiniatura(self):
        self.verMiniatura = f'{self.anotacao[:100]}...'
        return self.verMiniatura

    def save(self, *args, **kwargs):
        value = self.titulo
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.usuario} - {self.titulo} - {self.criacao}'
  

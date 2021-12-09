from django import forms
from django.contrib.auth import get_user_model
from .models import Post
User = get_user_model()

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'anotacao']
        labels={
            'titulo':'Título',
            'anotacao':'Corpo da Postagem'
        }
        widgets={
            'titulo':forms.TextInput(attrs={'type':'text', 'class':'form-control form-control-xl', 'placeholder':'Um título chave', 'rows':'6'}),
            'anotacao':forms.Textarea(attrs={'placeholder':'Uma bela postagem', 'class':'form-control form-control-xl', 'rows':'6'}),
        }
    
    def clean_field(self):        
        return self.cleaned_data
    
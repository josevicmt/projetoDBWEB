from django.contrib.auth import login
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
# Create your views here.

def index(request):
    user = request.user
    posts =  Post.objects.all()
    postForm = PostForm(request.POST or None)
    if postForm.is_valid():
        anotacao = postForm.cleaned_data.get('anotacao')
        titulo   = postForm.cleaned_data.get('titulo')
        post     = Post.objects.create(titulo=titulo, anotacao=anotacao, usuario=user)
        post.save()    
    post = Post.objects.last()
    contexto={
        'posts':posts,
        'postForm':postForm,
        'post':post,
    }
    return render(request, 'index.html', contexto)

def verPost(request, pk, slug):
    post = get_object_or_404(Post, id=pk, slug=slug)
    return render(request,'verPost.html', {'post':post})

def editarPost(request, pk, slug):
    postForm = PostForm(request.POST or None)
    if postForm.is_valid():
        anotacao = postForm.cleaned_data.get('anotacao')
        titulo   = postForm.cleaned_data.get('titulo')
        post = get_object_or_404(Post, id=pk, slug=slug)
        post.anotacao = anotacao
        post.titulo   = titulo
        post.save()

    return render(request,'verPost.html', {'post':post})
from django.contrib.auth import login
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
    paginator = Paginator(posts, 1)
    page = request.GET.get('page')
    try:
        pagi = paginator.page(page)
    except PageNotAnInteger:
        pagi = paginator.page(1)
    except EmptyPage:
        pagi = paginator.page(paginator.num_pages)

    contexto={
        'posts':posts,
        'postForm':postForm,
        'postspaginator':pagi, 
    }
    return render(request, 'index.html', contexto)

def verPost(request, pk, slug):
    post = get_object_or_404(Post, id=pk, slug=slug)
    return render(request,'verPost.html', {'post':post})

@login_required
def excluirPost(request, pk, slug):
    post = get_object_or_404(Post, id=pk, slug=slug)
    apagar = request.POST.get('apagar') or None
    if apagar is not None:
        post.delete()
        return redirect('index')
    return render(request,'excluir.html', {'post':post})

@login_required
def editarPost(request, pk, slug):
    post = get_object_or_404(Post, id=pk, slug=slug)
    postForm = PostForm(request.POST, instance=post )
    if postForm.is_valid():
        anotacao = postForm.cleaned_data.get('anotacao')
        titulo   = postForm.cleaned_data.get('titulo')
        post.anotacao = anotacao
        post.titulo   = titulo
        post.save()

    return render(request,'editar.html', {'post':postForm})
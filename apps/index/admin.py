from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdminRegister(admin.ModelAdmin):
    list_display = ('id','usuario', 'titulo', 'criacao')
    list_display_links = ('usuario',)
    search_fields = ('usuario','titulo')
    list_filter = ('usuario',)
    list_per_page = 20
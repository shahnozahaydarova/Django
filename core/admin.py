from django.contrib import admin
from .models import Post
@admin.register(Post)
class ArticlePost(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('name',)}

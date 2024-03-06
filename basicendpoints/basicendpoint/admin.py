from django.contrib import admin

from .models import Blog, Article, Post

admin.site.register(Blog)
admin.site.register(Article)
admin.site.register(Post)
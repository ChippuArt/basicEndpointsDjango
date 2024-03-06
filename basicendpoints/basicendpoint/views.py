from rest_framework import viewsets, filters
from .models import Blog, Post, Article
from .serializers import BlogSerializer, PostSerializer, ArticleSerializer
from django_filters.rest_framework import DjangoFilterBackend


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # Remember, the flexibility of Django and DRF means you can tailor your API's
    # endpoints to meet your specific needs, whether that's handling simple CRUD operations or
    # complex queries involving multiple model fields and relations.
    filter_backends = [DjangoFilterBackend]
    # examples for filtering fields for the Post Model. if you implented the User model the filterset could be looking
    # like author__name and so on
    filterset_fields = ['author', 'created_at']
    # Outputs pre sorted by our desire
    ordering_fields = ['created_at', 'title']


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

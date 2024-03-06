from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'blogs', views.BlogViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'articles', views.ArticleViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
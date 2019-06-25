from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, UserViewSet


router = DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

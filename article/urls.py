from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet


router = DefaultRouter()
router.register(r'articles', ArticleViewSet, base_name='article')
urlpatterns = router.urls

# urlpatterns = [
#     path('articles/', ArticleViewSet),
# ]

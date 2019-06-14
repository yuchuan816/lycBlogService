from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'get_article_list', views.ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('get_article_list/', views.ArticleViewSet)
]

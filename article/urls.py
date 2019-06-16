from django.urls import path
from .views import ArticleView

urlpatterns = [
    path('get_article_list', ArticleView.as_view()),
]

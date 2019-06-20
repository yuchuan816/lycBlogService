from django.urls import path
from . import views


urlpatterns = [
    path('add_article/', views.add_article),
    path('delete_article/', views.delete_article),
    path('modify_article/', views.modify_article),
    path('get_article_list/', views.get_article_list),
]

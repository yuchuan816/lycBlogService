from django.contrib import admin
from .models import Article, Category, Tag
from django.apps import apps
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'pk' , 'created_time', 'modified_time', 'category', 'author']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)

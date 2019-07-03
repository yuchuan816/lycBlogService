from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Article, Tag, Category

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Article
        fields = ('title', 'body', 'author', 'tags',
                    'category', 'created_time', 'modified_time',)

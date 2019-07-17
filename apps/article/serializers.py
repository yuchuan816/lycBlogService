from rest_framework import serializers
from .models import Article, Tag, Category
from commentary.serializers import CommentSerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    tags = serializers.StringRelatedField(many=True, required=False)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ('title', 'body', 'author', 'tags', 'comments',
                  'category', 'created_time', 'modified_time',)

from rest_framework import serializers
from .models import Article, Tag, Category
# from commentary.serializers import Comment, CommentSerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class ArticleListSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    author = serializers.StringRelatedField()
    tags = serializers.StringRelatedField(many=True, required=False)

    class Meta:
        model = Article
        fields = ('id', 'title', 'tags', 'author', 'category',
                  'created_time', 'modified_time',)
        read_only_fields = ('created_time', 'modified_time',)


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    tags = serializers.StringRelatedField(many=True, required=False)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects, source='category')
    tags_id = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects, source='tags', many=True)

    # comments = serializers.SerializerMethodField()

    # def get_comments(self, obj):
    #     queryset = Comment.objects.filter(comments_id=None)
    #     comment_serializer = CommentSerializer(queryset, many=True)
    #     return comment_serializer.data

    class Meta:
        model = Article
        fields = ('id', 'title', 'body', 'author', 'tags', 'category_id', 'tags_id',
                  'category', 'created_time', 'modified_time',)
        read_only_fields = ('created_time', 'modified_time',)
        extra_kwargs = {'category_id': {'write_only': True},
                        'tags_id': {'write_only': True}, }

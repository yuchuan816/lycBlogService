from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from .models import Comment, CommentLikeAndOpposition
from django.contrib.auth.models import User


class CommentLikeAndOppositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLikeAndOpposition
        fields = ('user', 'comment', 'type',)


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.StringRelatedField(source='user')
    reply = RecursiveField(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'content', 'username', 'comments', 'user',
                  'created_time', 'reply', 'article',)
        read_only_fields = ('created_time',)
        extra_kwargs = {'article': {'write_only': True},
                        'comments': {'write_only': True},
                        'user': {'write_only': True}}

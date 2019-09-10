from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from .models import Comment, CommentLikeAndOpposition


class CommentLikeAndOppositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLikeAndOpposition
        fields = ('user', 'comment', 'type',)


class CommentSerializer(serializers.ModelSerializer):
    reply = RecursiveField(many=True)

    class Meta:
        model = Comment
        fields = ('id', 'content', 'user', 'created_time', 'reply')

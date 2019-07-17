from rest_framework import serializers
from .models import Comment, CommentLikeAndOpposition


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentLikeAndOppositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user', 'comment', 'type',)


class CommentSerializer(serializers.ModelSerializer):
    reply = RecursiveField(many=True)

    class Meta:
        model = Comment
        fields = ('content', 'user', 'created_time', 'reply')



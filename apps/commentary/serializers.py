from rest_framework import serializers
from .models import Comment, CommentLikeAndOpposition


class CommentSerializer(serializers.ModelSerializer):
    # reply = serializers.StringRelatedField(many=True, required=False)
    # reply = CommentSerializers(many=True, required=False)

    class Meta:
        model = Comment
        fields = ('content', 'user', 'created_time', 'reply')


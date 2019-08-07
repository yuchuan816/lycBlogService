from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_username(self, value):
        if not 6 <= len(value) <= 16:
            raise serializers.ValidationError('用户名需6 - 16位之间')
        return value

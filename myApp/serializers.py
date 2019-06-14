from rest_framework import serializers
from myApp.models import Student


# 给学生类创建序列化类
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("id", "name", "sex", "age", "content", "isDelete")

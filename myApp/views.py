from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView

# Create your views here.


@api_view(["GET", "POST"])
def get_student_list(request):
    stus = Student.objects.all()
    # 序列化
    serializer = StudentSerializer(stus, many=True)
    # 不需要指定json格式，返回客户端可以返回json或者HTML，返回HTML内容的话，会在浏览器中经过渲染成页面
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def add_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        # 存数据
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


'''
class StudentsList(APIView):
    def get(self, request, format=None):
        stus = Student.objects.all()
        serializer = StudentSerializer(stus, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
'''

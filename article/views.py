from rest_framework import status, generics
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializers import ArticleSerializer
from .models import Article

# Create your views here.

# class ArticleView(APIView):
#     def get(self, request, *args, **kwargs):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(instance=articles, many=True)
#         return Response(serializer.data)


class ArticleView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

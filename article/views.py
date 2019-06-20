from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer
from .models import Article

# Create your views here.


@api_view(['GET', 'POST'])
def get_article_list(request):
    req = request.data
    pk = req.get('id', None)
    has_value = pk is not None
    articles = Article.objects.get(pk=pk) if has_value else Article.objects.all()
    serializer = ArticleSerializer(instance=articles, many=not has_value)
    return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(['GET', 'POST'])
# def add_article(request):
#     serializer = ArticleSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     return Response({"error": serializer.errors}, status=status.HTTP_200_OK)


# @api_view(['GET', 'POST'])
# def modify_article():
#     article = Article.objects.all()


# @api_view(['GET', 'POST'])
# def delete_article():
#     article = Article.objects.all()

# class ArticleView(APIView):
#     def get(self, request, *args, **kwargs):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(instance=articles, many=True)
#         return Response(serializer.data)


class ArticleView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

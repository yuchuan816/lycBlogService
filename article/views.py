from rest_framework import status, viewsets
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer
from .models import Article

# Create your views here.


# @api_view(["GET", "POST"])
# def get_article_list(request):
#     return Response({'name': 'liuyuchuan'}, status=status.HTTP_200_OK)

class ArticleViewSet(viewsets.ModelViewSet):
    article_set = Article.objects.all()
    serializer_class = ArticleSerializer

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleListSerializer

# Create your views here.
@api_view(['GET'])
def article_list(request):
    # 게시글 전체 목록 가져오기
    # JSON으로 변환해서 응답
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)
    


@api_view(['GET'])
def article_detail(request, article_pk):
    # 게시글 하나 가져오기
    # JSON으로 변환해서 응답
    # article = Article.objects.get(pk=article_pk)
    # serializer = ArticleListSerializer(article)
    # return Response(serializer.data)
    pass
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from .models import Article
from .serializers import ArticleSerializer

# Create your views here.
def article_html(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/article.html', context)


def article_json_1(request):
    articles = Article.objects.all()
    articles_json = []

    for article in articles:
        articles_json.append(
            {
                'id': article.pk,
                'title': article.title,
                'content': article.content,
                'created_at': article.created_at,
                'updated_at': article.updated_at,
            }
        )
    # 리턴에 articles_json 바로 넣으면 안됨
    # 파이썬이 인식할 수 있는 형태로 바꿔야 함
    return JsonResponse(articles_json, safe=False) # safe ?

# serialize 직렬화를 통해 직접 append하지 않고 원하는 포맷(json)으로 바꿨다
def article_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type='application/json')


# DRF를 사용해서 과정 진행
@api_view(['GET'])
def article_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True) # many ?
    return Response(serializer.data)


@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
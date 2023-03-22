from django.shortcuts import render, redirect
from .models import Article
# Create your views here.
# 전체 목록 보기
# index 창 그대로 보이면 된다.
def index(request):
    return render(request, 'articles/index.html')

# 새 게시글 작성화면 보기
# 게시글 작성화면 그대로 보이면 된다.
def new(request):
    return render(request, 'articles/new.html')

# 새 게시글 만들기
# 클라이언트에 던진 데이터를 받아서, DB에 저장
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article(title = title, content = content)
    article.save()

    return redirect('articles:index')

# 게시글 하나의 상세 정보를 담고있는 상세 페이지 보여주기
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

# 게시글 수정화면 보여주기
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/edit.html', context)

# 수정 정보 받아서 DB에 수정
def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', pk)

# 삭제하기
def delete(request, pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        article.delete()
    return redirect('articles:index')
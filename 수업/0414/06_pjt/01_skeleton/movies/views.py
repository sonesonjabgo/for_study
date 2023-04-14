from django.shortcuts import render, redirect
from .models import Movie, Comment, Movie_like_users
from .forms import MovieForm, CommentForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)


def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    # 댓글 기능 넣어야 함
    comment_form = CommentForm()
    comments = movie.comment_set.all()
    context = {
        'movie': movie,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'movies/detail.html', context)


def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')


def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'movie': movie,
        'form': form,
    }
    return render(request, 'movies/update.html', context)

@require_POST
def comments_create(request, pk):
    # 이건 생성 창 보여주는 기능은 필요없음 
    # post만 받으면 됨
    # account 완료하고 하기
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=pk)
        comment_form = CommentForm(request.POST) # 폼에 POST요청 넣어주고
        if comment_form.is_valid():
            comment = comment_form.save(commit=False) 
            # 저장하기 전에 코멘트가 속한 영화와 작성한 user 정보 넣어주기
            comment.movie = movie
            comment.user = request.user
            comment.save()
        return redirect("movies:detail", movie.pk)
    return redirect("accounts:login")

@require_POST
def comments_delete(request, movie_pk, comment_pk):
    # 댓글 데이터 삭제하려면
    # 데이터 작성한 계정과 현재 삭제 요청한 계정과 같은 지 확인
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)
        if comment.user == request.user:
            comment.delete()
    return redirect('movies:detail', movie_pk)


def likes(request, pk):
    # 게시물 정보 가져와서
    # 해당 계정이 게시물에 대해 좋아요를 눌렀는 지 확인
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=pk)
        if movie.movie_like_users_set.filter(user_id=request.user.pk).exists():
            r1 = Movie_like_users.objects.get(movie_id=movie.pk, user_id=request.user.pk)
            r1.delete()
        else:
            # movie.movie_like_users_set.add(request.user)
            Movie_like_users.objects.create(movie_id=movie.pk, user_id=request.user.pk)
        return redirect('movies:index')
    return redirect('accounts:login')
from django.shortcuts import render, redirect
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request):
    # 로그인 창을 보여주거나 GET
    # 로그인 해주거나 POST
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:index') # 이따가 get('next') 넣기
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    # 로그아웃 기능만 POST
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('movies:index')

def signup(request):
    # 회원가입 창 보여주거나 GET
    # 회원가입 기능 POST
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

@require_POST
def delete(request):
    # 계정 삭제 기능 POST
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('movies:index')

@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    # 계정 정보 수정 창 GET
    # 게정 정보 수정 POST
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
    # 계정 비밀번호 변경 창 GET
    # 계정 비밀번호 변경 POST
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/password.html', context)


def profile(request, username):
    # 프로필 창 GET
    pass

@require_POST
def follow(request, user_pk):
    # 팔로우 기능 POST
    # 모델 self 참조 이해해야 함
    if request.user.is_authenticated: # 현재 로그인 정보가 있다면
        person = get_user_model().get(pk=user_pk)
        if person != request.user: # 현재 로그인 할 계정과 팔로우 요청을 보낸 계정이 같은 계정이 아니라면
            if person.followers.filter(pk=request.user.pk).exists():
                # 이미 팔로우 했다면
                person.followers.remove(request.user)
            else:
                person.followers.add(request.user)
        return redirect('movies:index')
    return redirect('accounts:login')
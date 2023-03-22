from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def login(request):
    # GET 요청이면 화면 보여주기
    # POST 요청이면 로그인 처리
    if request.method == 'POST':
        # 로그인 처리
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
        return redirect('articles:index')

    else:
        #AuthenticationForm을 사용하자
        form = AuthenticationForm()
        context = {
            'form' : form
        }
        return render(request, 'accounts/login.html', context)

def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('articles:index')
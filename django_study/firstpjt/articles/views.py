from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    context = {
        'name': '김싸피'
    }
    return render(request, 'articles/hello.html', context)
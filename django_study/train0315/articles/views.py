from django.shortcuts import render

# Create your views here.
def hello(request, name):
    food = ['김치', '떡볶이', '삼겹살', '초밥']
    price = ['200', '500', '1000', '800']
    context = {
        'name' : name,
        'food' : food,
        'price' : price
    }
    return render(request, 'articles/hello.html', context)
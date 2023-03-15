from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # path('articles/', include('articles.urls')),
    path('index/<str:name>/', views.index, name='index'),
    path('detail/', views.index, name='detail'),
    path('update/', views.index, name='up'),
    path('delete/', views.index, name='del'),
]

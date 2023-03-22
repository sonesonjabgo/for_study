from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # 게시글 전체 조회
    # 1. 전체 게시글 조회
    path('index/', views.index, name='index'),
    # 2. 게시글 하나 보기
    path('<int:pk>/', views.detail, name='detail'),
    # 3. 새 게시글 작성화면 보기
    path('new/', views.new, name='new'),
    # 4. 새 게시글 작성하기
    path('create/', views.create, name='create'),
    # 5. 수정 화면 보기
    path('edit/<int:pk>/', views.edit, name='edit'),
    # 6. 수정하기
    path('update/<int:pk>/', views.update, name='update'),
    # 7. 삭제하기
    path('detail/<int:pk>/', views.delete, name='delete'),
    
]
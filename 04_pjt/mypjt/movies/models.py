from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)     # 영화 제목
    audience = models.CharField(max_length=20)  # 관객 수
    release_date = models.DateField(auto_now=True)           # 개봉일
    genre = models.CharField(max_length=30)     # 장르
    score = models.IntegerField(validators=[
        MinValueValidator(0),MaxValueValidator(5)]
        )                 # 평점
    poster_url = models.CharField(max_length=50) # 포스터 경로
    description = models.TextField()            # 줄거리
    actor_image = models.ImageField(blank=True, null=True)           # 대표 배우 이미지
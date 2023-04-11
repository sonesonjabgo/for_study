from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):   # 인증 관련 기능을 가지고 있는 기본 user를 상속받아 작성
    pass
#user/models.py
# DB 변경을 알려주는 명령어 : python manage.py makemigrations
# 변경된 DB를 반영해주는 명령어 : python manage.py migrate

from django.db import models
from django.contrib.auth.models import AbstractUser #장고에서 제공하는 기본적인 유저 모델
from django.conf import  settings #장고가 관리하는 세팅을 가져오는 것

# Create your models here.
"""
#장고에서 제공하는 유저 모델을 사용하기 전 코드
class UserModel(models.Model): #models.Model을 상속받음
    class Meta: #DB에 정보를 넣어주는 역할
        db_table = "my_user"

    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=256, null=False)
    bio = models.CharField(max_length=256, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
"""

class UserModel(AbstractUser) : #장고에서 제공하는 기본 유저 모델을 상속받은 후, bio 필드 추가
    class Meta:  # DB에 정보를 넣어주는 역할
        db_table = "my_user"

    bio = models.CharField(max_length=256, default='')
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='followee')
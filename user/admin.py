from django.contrib import admin
from .models import UserModel
# 관리자 계정 생성 명령어 : python manage.py createsuperuser

# Register your models here.
admin.site.register(UserModel) # 이 코드가 나의 UserModel을 Admin에 추가 해 줍니다
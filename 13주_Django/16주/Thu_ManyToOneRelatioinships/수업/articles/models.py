from django.db import models
# 문자열을 리턴(models.py에서만 사용)
from django.conf import settings
# 모델에서는 이 형식을 사용하지 않믐(객체를 리턴)
# from django.contrib.auth import get_user_model
# 아래와 같은 직접 참조는 안돼
# from accounts.models import User

# Create your models here.
class Article(models.Model):
    # 유저 모델을 직접적으로 가져오는거 금지, 반환 함수 작성 => setting에서 .AUTH_USER_MODEL를 가져옴
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    #  기본 출력을 title로 바꾼다
    # def __str__(self):
    #     return self.title


class Comment(models.Model):
    # 왜래 키 필드(참조 받는 것, 아티클이 지워지면 같이 지워지게)
    # article(N:1이니 단수형) 설정 => 외래키로 article_id로 DB에 데려오게 됨
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


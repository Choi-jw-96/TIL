from django.db import models

# Create your models here.
# model을 Article에 상속한다(models는 모듈)
class Article(models.Model):
    # 필드 이름 / 데이터 타입(모델 필드 클래스)  / 제약 조건(모댈 필드 클래스의 키워드 인자)
    #  둘다 문자 열 CharField(글자 수 제약 필요) TextField
    title = models.CharField(max_length=10)
    contnet =models.TextField()
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
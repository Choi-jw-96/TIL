from django.contrib import admin
from .models import Article
# Register your models here.

#우리가 만든 Article 클래스가져오기
# 의미 : admin사이트에 등록하겠다
admin.site.register(Article)
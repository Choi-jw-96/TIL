# model

## 개요
model을 통한 DB관리
- SQLlige를 통해 관리

## 1. model
DB를 **테이블을 정의**하고 **조작**할 수 있는 기능을 제공하는 테이블 설계 청사진 
```py
articles/model.py
class Article(models.Model):
#  id는 자동 생성 
# 필드 이름 / 데이터 타입(모델 필드 클래스)  / 제약 조건(모댈 필드 클래스의 키워드 인자) 
#  둘다 문자 열 CharField(글자 수 제약 필요) TextField 
    title = models.CharField(max_length=10)
    contnet =models.TextField()
```
- django.db.models 모듈의 model이라는 부모 클래스를 상속받아 작성

- [model기능에 관련된 모든 설정이 담긴 클래스](https://github.com/django/django/blob/main/django/db/models/base.py#L459)

### 구성
- 클래스 변수명 : 테이블의 각 필드 이름 
- model Field클래스 : 테이블 필드의 데이터 타입
- model Field 클래스의 키워드 인자(필드 옵션) : 제약조건


## 2. migration
model 클래스의 변경사항(필드 생성, 추가 수정 등)을 DB에 최종 방영

### migration과정
```bash
# 초안 설계도를 만든다(model → migrations)
python manage.py makemigrations
# db에 최종 반영(migrations → db)
python manage.py migrate
```
---
```bash
# migration 상황을 보여줌 'X'라면 성공적으로 migration된 것
python manage.py showmigrations
# migration 할때 어떻게 번역되어 들어가는지 보여줌
python manage.py sqlmigrate articles 0001
```


### 추가 모델 필드 작성
```python
#model.py
creat_at = models.DateTimeField(auto_now_add=True)
```
```bash
python manage.py makemigrations
You are trying to add the field 'creat_at' with 'auto_now_add=True' to article without a default; the database needs something to populate existing rows.
# 이미 있는 것에 추가할건지 정해줘(추가할 때 기본값 설정)
 1) Provide a one-off default now (will be set on all existing rows)
#  장고의 기본값일 줄까?
 2) Quit, and let me add a default in models.py
#  너가 직접 py에 입력할래?
```

**model class에 변경사항이 생겼다면, 반드시 새로운 설계도를 생성하고 이를 DB에 반영한다**


### 모델 필드 클래스
- CharField : 길이 제한이 있는 문자열 (max_lenth가 필수 인자)
- TextField : 글자수가 많을 때 사용
- DateTimeField : 날짜오 시간을 넣을 때 사용(auto_now: 수정시에도 갱신 / auto_now_add: 처음에만 자동으로 날짜 저장 )


## 3. Admin site
### Automatic admin interface
django는 추가 설치 및 설정 없이 **자동으로 관리자 인터페이스를 제공**

#### 1. 관리자 계정  생성
```bash
python manage.py createsuperuser
```
계정 생성을 db_user에서 확인

#### 2. admin에 모델 클래스 등록
```py
admin.py
from . import models

admin.site.register(models.Todo)
```



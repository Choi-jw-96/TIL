# Django set
## 가상환경 만들기

```bash
## 1. 내가 만드는 경우
#### 1. 가상환경을 만든다
python -m venv venv
#### 2. 가상환경 활성화
shift+ctrl+p → 파이썬 인프리터
source venv/Scripts/activate
#### 3. django 설치
pip install django==3.2.18
#### 4. 의존성 파일 생성
pip freeze > requirements.txt
```
``` bash
#### + .gitignore 설정 & git init
#### 5. django 프로젝트 생성
django-admin startproject firstpjt .
```=> 뛰어쓰기 필수! 뒤에 점을 꼭 찍어줘야 py 출력```
#### 6. dhango 서버 실행
python manage.py runserver
#서버와의 연결을 위해 URL을 켜준다
# 끄기
crtl + c
deactivate
```

# 내가 깃 받았을때 패키지 설치
```bash
#### 1. 가상환경을 만든다
python -m venv venv
#### 2. 설정을 적용한다
pip install -r requirements.txt
```

[이그노어 사이트](https://www.toptal.com/developers/gitignore/)

---

# 앱 생성
```bash
# 앱 생성 (복수형으로 작성)
python manage.py startapp articles
# 앱 등록
## firstpjt → INSTALLED_APPS 첫줄에 밑 코드 작성
'articles',
```

# 요청과 응답
```bash
# 1. firstpjt → URLs작성
## 주소를 입력(/articles/) 시 views 모듈에 index를 호출
path('articles/', views.index),
# 2. articles → View 작성
## 특정 경로에 있는 template와 requset 객체를 결합해 응답을 반환하는 index view 함수 작성
def index(request):
    return render(request, 'articles/index.html')
# 3. Template 작성
## articles → Templates 폴더생성 후 articles에대한 페이지 생성
index.html
# 4. 페이지 확인
python manage.py runserver
```
---

# migration
## 1. model 작성
필드 이름 / 데이터 타입(모델 필드 클래스)  / 제약 조건(모댈 필드 클래스의 키워드 인자) 
(id는 자동 생성)

```py
class model_name(medels.Model):
    field_name = models.model_type(option)
```
## 2. model db에 반영
```bash
# 초안 설계도를 만든다(model → migrations)
python manage.py makemigrations
# db에 최종 반영(migrations → db) 
python manage.py migrate
```
### 필드 추가 & 기본값

model class에 변경사항이 생겼다면, 반드시 새로운 설계도를 생성하고 이를 DB에 반영

model에 새 필드를 추가
```bash
python manage.py makemigrations

You are trying to add the field..to article without a default
# 기본값을 정해주지 정해줘
 (1) Provide a one-off default now (will be set on all existing rows)
#  장고의 기본값일 줄까?
 (2) Quit, and let me add a default in models.py
#  너가 직접 py에 입력할래?

python manage.py migrate
```

# 관리자 계정 생성
```bash
python manage.py createsuperuser
```
- 아이디 비밀번호 작성
- python manage.py runserver로 서버로 들어가서 로그인


## 페이지 생성
admin.py에서 model에 있는 것을 데리고 온다.
```py
from . import models
# admin 사이트에 등록하겠다
admin.site.register(models.model_name)
```
- 페이지에서 CRUD테스트
- db.sqlit3에서 auth_user와 생성페이지를 확인한다

# Static Files
서버 측에서
정적 파일을 제공하기 위해서 경로(URL)이 있어야한다

## 1. 정적파일 제공하기
- 기본경로 : app/static/
- 추가경로 : STATICFILES_DIRS

### 기본경로
1. html파일에 {% load static %}
2. <img src="{% static 'articles/sample-1.png' %}" alt="img"> 형식으로 적는다

### 추가경로 제공하기
1. setting에 아래와 같이 작성
```
  STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

## 2. Media files
정적 파일 중에서도 사용자가 업로드하는 파일

- ImageField() : 이미지 업로드에 사용하는 모델 필드

1. setting.py에 MEDIA_ROOT,MEDIA_URL설정
```py
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/
```
2. urls.py에 업데이트
```py
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
```

## 3. 이미지업로드 제공하기
3. models.py 업데이트
```py
    image = models.ImageField()
```
4. 사이트 업데이트
```bash
python -m pip install Pillow

python manage.py makemigrations
python manage.py migrate

pip freeze >  requirements.txt
```

5. html form에 아래는 추가
```py
enctype="multipart/form-data"
```

6. veiw함수에 아래 추가
```py
form = ArticleForm(request.POST, request.FILES)
```

7. 사용자에게 제공(이미지가 있을때만 띄움)
```py
  {% if article.image %}
    # 온라인상 URL을 제공받음
    <img src="{{article.image.url}}" alt="img">
  {% endif %} 
```

## 4. 정적파일
서버측에서 변경되지 않고 고정적으로 제공되는 파일


---
### 장고 리사이징
원본보다 낮은 설정(크기, 화질)으로 용량을 적게 차지하게 사용하는 기법
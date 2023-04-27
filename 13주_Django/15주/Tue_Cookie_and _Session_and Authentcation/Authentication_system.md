# Authentication_system(인증 시스템)
사용자 인증과 관련된 기능을 모아 놓은 시스템
인증과 관한 부여를 함께 제공 및 처리

Authorization : 인증된 사용자가 수행할 수 있는 작업을 결정 권한 부여

사전 설정
app urls.py
```py
app_name = "accounts"
```
project urls.py
```py
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
]
```

## 1. Custom User Model
django에 기본적으로 제공하는 User model은 직접 수정을 할 수 없는 문제가 있다.
대체하는 것을 강하게 권장한다

### 대체하기
**프로젝트 중간에 AUTH_USER_MODEL 도중에 변경 불가!**
models.py
```py
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

settings.py
```py
AUTH_USER_MODEL = 'accounts.User' # 기본값을 'auth_user'에서 대체한다
```

기본 모델이 아니라 admin site에 등록 필수
admin.py
```py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```


## 2. Login
urls.py
```py
    path('login/', views.login, name='login'),
```

views.py
```py
from django.contrib.auth import login as auth_login, logout as auth_logout

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
          # login(request, user) : 인증된 사용자를 로그인 하는 함수
          # get_user() : 유효성 검사를 통과한 경우 로그인한 사용자 객체를 반환
            auth_login(request, form.get_user())
            return redirect('articles:index')
        
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)
```

template
```html
  <form action="{% url 'accounts:login' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
```
- login : 현재 session data를 DB에 생성
- logout : 현재 session data를 DB와 클라이언트 쿠키에서 삭제

## 3. Temlplate with Authenticetion data
템플릿에서 인증 관련 데이터를 출력하는 방법

templates
```html
<h3>안녕하세요, {{user}}님!</h3>
```
장고에서 미리 자주 이용하는 목록을 미리 템플릿에 로드 해 뒀기 때문
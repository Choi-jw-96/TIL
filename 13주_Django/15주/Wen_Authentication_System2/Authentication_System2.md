# Authentication_System2

## 1. 개요
## User 객체와 CUD
- 회원 가입
- 회원 탈퇴

## 2. 회원 가입
### userCreationForm()
User를 대체해줬으니 UserCreationForm를 사용하기위해 대체작업을 해준다
forms.py
```py
# 장고는 직접참조를 권장하지 않음
# from .models import User
# 아래와 같은 간접 참조를 이용한다
# get_user_model 현재 프로젝트에 활성화 되어있는 User객체를 반환해준다
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # 현재 우리가 사용하는 User class로 재정의(우리가 accounts를 재정의했기 때문)
        model = get_user_model()
```

urls.py
```py
    path('signup/', views.signup, name='signup'),
```

views.py
```py
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 자동 로그인
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)
```

template
```html
  <form action="{% url 'accounts:signup' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
```

## 4. 회원정보 수정
일반 사용자가 접근하면 안될 정보들까지 수정하는 것을 막기위해 조정해준다
forms.py
```py
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')
```

views.py
```py
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')

    else:
        form = CustomUserChangeForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/update.html', context)

```


## 5. 비밀번호 변경
장고 내에서 비밀번호 페이지 변경은 별도의 주소로 안내
urls.py
```py
    path('password/', views.change_password, name='change_password'),
```

views.py
```py
# 암호 변경 시 세션 무효화를 방지(없다면 변경 후 기존의 인증 정보가 일치하지 않아 로그인 상태 유지 X)
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # 비밀번호가 변경되어도 로그아웃 되지않도록 기존 session 업데이트
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form
    }
    return render(request, 'accounts/change_password.html', context)
```

template
```html
  <form action="{% url 'accounts:change_password' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
```

## 6. 로그인 사용자에 대한 접근 제한
### request.user.is_authenicated
사용자가 인증 되었는지 여부는 알수 있는 속성
- user : True
- anomymouse : False
templates
```html
 {% if request.user.is_authenticated %}
    <form action="{% url 'accounts:logout' %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="LOGOUT">
    </form>

    <form action="{% url 'accounts:delete' %}"  method="POSt">
      {% csrf_token %}
    </form>
    <input type="submit" value="[회원탈퇴]">  
    <a href="{% url 'accounts:update' %}">[회원정보수정]</a>
  {% else %}
    <a href="{% url 'accounts:login' %}">[LOGIN]</a>
    <a href="{% url 'accounts:signup' %}">[signup]</a>
  {% endif %}
```
### @login_required
인증된 사용자에 대해서만 view함수를 실행 시키는 데코레이터
views.py
```py
from django.contrib.auth.decorators import login_required


@login_required
def create(request):
```
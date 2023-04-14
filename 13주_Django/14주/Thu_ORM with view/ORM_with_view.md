# OMR with veiw

## 1. HTTP request methods
### redirect()
인자에서 작성된 주소로 다시 돌려보냄

```py
# veiws.py
from django.shortcuts import render, redirect
def create(request):
  title = request.POST.get('title')
  content = request.POST.get('content')

  article = Article(title=title, content=content)
  article.save()

  return redirect(request, 'article/create.html')
```

### HTTP
네트워크상에서 데이터를 주고 받기 위한 약속
요청과 응답이 핵심

### HTTP request methods
데이터(리소스)에 어떤 요청(행동)을 원하는지를 나타내는 형식

- GET Method : 특정 리소스를 **조회**하는 요청(**반드시 데이터를 조회할때 사용**)
- POST Method : 특정 리소스에 **변경사항**을 만드는 요청(주소에 표현 X, HTTPbody에 담겨 보내짐)

| GET Method | POST Method |
|-|-|
|특정 리소스를 조회하는 요청|특정 리소스에 **변경사항을 만드는 요청**|
|**반드시 데이터를 조회할때 사용**|조회 외 사용|
|주소에 표현|주소에 표현 X, HTTPbody에 담겨 보내짐|
|글자수 제한O(255)|글자수 제한 X|


### Security Token(CSRF Token)
403 Forbidden(서버에 요청이 전달 됐지만, 권한때문에 거절)
CSRF Token를 이용아여 임의의 난수값을 부여하여 유효한지 검증할 수 있게 도와줌

**POST Method는 데이터베이스 대한 변경 사항을 만드는 요청이라서 토큰을 사용해 최소한의 신원을 확인을 하는 것**

## 2. Delete
```py
# urls.py
path('<int:pk>/delete/', veiws.delete, name='delete')
```
```py
# veiws.py
def detail(request, pk):
  article = Article.objects.get(pk=pk)
  article.delete()
  return redirect('article:index')
```
```html
<form action= "{% url 'articles:delect' article.pk%}" method="POST">
  {% csrf_token %}
  <input type="submit" value='[delect]'>
</form>
```


## 3. Update
### 필요 함수
1. edit : 사용자의 입력을 받는 페이지
```py
# urls.py
path('<int:pk>/edit/', veiws.edit, name='edit')
```
```py
# veiws.py
def edit(request, pk):
  article = Article.objects.get(pk=pk)
  context = {
    'article' = article
  }
  return render(request, 'article/edit.html', context)
```
이전에 쓴 내용 저장한 페이지 출력
```html
<form action= "{% url 'articles:create' %}" method="POST">
  {% csrf_token %}
  <div>
    <label for='title'>Title: </label>
    <input type="text" name="title" id="title" value='{{article.title}}'>
    <textarea>{{article.content}} </textarea>
  </div>
  <input type="submit">
</form>
```

2. update : 사용자가 입력한 데이터를 받아 DB에 저장

```py
# urls.py
path('update/', veiws.update, name='update')
```
```py
# veiws.py
def update(request):
  title = request.POST.get('title')
  content = request.POST.get('content')

  article = Article(title=title, content=content)
  article.save()

  return redirect('article:detail', article.pk)
```
```html
<form action= "{% url 'articles:update' %}" method="POST">
  {% csrf_token %}
  <div>
    <label for='title'>Title: </label>
    <input type="text" name="title" id="title" value='{{article.title}}'>
    <textarea>{{article.content}} </textarea>
  </div>
  <input type="submit">
</form>
```

### date 시 날짜 저장
```py
value={{todo.deadline|date:"Y-m-d"}}
```

### boolean 타입 변경
```py
# urls.py
path('<int:pk>completed/', views.completed, name='completed'),
path('<int:pk>uncompleted/', views.uncompleted, name='uncompleted'),
```
```py
# views.py
def completed(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.completed = True
    todo.save()
    return redirect('todos:index')


def uncompleted(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.completed = False
    todo.save()
    return redirect('todos:index')
```
```html
{% for todo in todos %}
  <p>▷ <a href="{% url 'todos:detail' todo.pk %}">pk-{{todo.pk}}</a></p>
  {% if todo.completed %}
    <p> / 완료 상태 : 완료!</p>
    <form action="{% url 'todos:uncompleted' todo.pk %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="미완료로 변경">
    </form>
  {% else %}
    <p class="col-3"> / 완료 상태 : 미완료.</p>
    <form action="{% url 'todos:completed' todo.pk %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="완료로 변경">
    </form>
  {% endif %}
{% endfor %}
```
---
참고
### 다양한 메서드를 사용하는 경우
#### 데이터 조회 시 메서드 [GET]사용시
 path('<int:pk>/', views.detail, name='detail'),
#### 데이터 삭제 시 메서드 [DELETE] 사용시
path('<int:pk>/', views.delete, name='delete'),
#### 데이터 수정 시 메서드 [PATCH] 사용시
path('<int:pk>/', views.update, name='update'),
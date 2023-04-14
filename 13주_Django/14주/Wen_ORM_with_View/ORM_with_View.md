f# ORM with View
## 1. app URLs 분할 연결
1. 앱에 urls.py를 만든다
2. 프로젝트에 include를 import해준다
3. 앱과 연결해 준다. (path('articles/', include'articles.urls'),)
4. 앱의 urls에 views.py를 연결 (from . import views)

## 2. Read
### 전체 게시글 조회
```py
# views.py
def index(request):
  articles = Article.objects.all()
  context = {
    'articles' : articles,
  }
  return render(request, 'article/index.html', context)
```
```html
{% for article in articles %}
  <p>글 제목 : article.title</p>
{% endfor %}
```

### 단일 게시글 조회
```py
# urls.py
path('<int:pk>/', veiws.detail, name='detail')
```
```py
# veiws.py
def detail(request, pk):
  article = Article.objects.get(pk=pk)
  context = {
    'article' = article
  }
  return render(request, 'article/detail.html', context)
```
```html
<p>글 제목 : article.title</p>
```

### 제목을 누르면 해당 페이지로 이동하게
```html
<a href="{% url 'articles:detail' article.pk %}">
```

## 3. Create
### 필요 함수
1. new : 사용자의 입력을 받는 페이지
```py
# urls.py
path('new/', veiws.new, name='new')
```
```py
# veiws.py
def new(request):
  return render(request, 'article/new.html')
```
```html
<form action= "{% url 'articles:create' %}" method="POST">
  {% csrf_token %}
  <div>
    <label for='title'>Title: </label>
    <input type="text" name="title" id="title">
    <textarea> </textarea>
  </div>
  <input type="submit">
</form>
```
2. create : 사용자가 입력한 데이터를 받아 DB에 저장

```py
# urls.py
path('create/', veiws.create, name='create')
```
```py
# veiws.py
def create(request):
  title = request.POST.get('title')
  content = request.POST.get('content')

  article = Article(title=title, content=content)
  article.save()

  return render(request, 'article/create.html')
```
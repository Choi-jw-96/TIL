# Form
사용자로 부터 form 요소르르 통해 데이터를 받고 있으나 비정상적, 악의적 요청을 확인하지 않고 모두 수용 함

→ 유효성 검증이 필요

## 1. Django Form
사용자 입력 데이터를 수집/처리 및 유효성 검증을 수행하기 위한 도구

### 유효성 검사
입력받은 데이터가 정확하고 유효한지 확인하는 과정

forms.py
```py
from django import forms
class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
```
views.py
```py
from .forms import ArticleForm
def new(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```
### Form class 선언
templates
```html
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p}} 
    {% comment %} ptag로 묶어줘(위에서 떨어뜨려줘) {% endcomment %}
    <input type="submit">
  </form>
```

## 2. Widgets
HTML 'input' element의 표현 담당 
→ 단순이 input요소의 속성 및 출력되는 부분을 변경하는 것

[widget](https://docs.djangoproject.com/ko/3.2/ref/forms/widgets/#built-in-widgets)


## 3. Django ModelsForm
### Form 
사용자 입력 데이터를 DB에 저장하지 않을때 (ex. 로그인)
### ModelForm
사용자 입력 데이터를 **DB에 저장해야 할때 (ex. 회원가입)**

#### Meta class
modelform의 정보를 작성하는 곳
**,** 마지막에 꼭 붙이기
- field = ('',) : 나올 필드만 지정
- exclude = ('',) : 배제할 필드 지정
- '__all__'


forms.py
```py
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        # fields = ('title',) 이 필드만 나오게
        # exclude = ('title',) 이 필드는 제외해서
```
views.py
```py
from .forms import ArticleForm
def create(request):
    form = ArticleForm(request.POST)
    # 유효성 검사가 Ture/False
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'form' : form
    }
    return render(request, 'articles/new.html', context)
```
제목에 공백을 넣으면 에러메세지 == 유효성 검사 결과

### is_valid()
유효성 검사 후 유효 여부를 boolean으로 반환

### save()
데이터베이스 객체를 만들고 저장

views.py
```py
def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article': article,
        'form' : form,
    }
    return render(request, 'articles/edit.html', context)
```
instance 여부를 통해 수정할 지 결정
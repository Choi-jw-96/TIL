# ORM

## 개요

### ORM(object-relational-mapping)
객체 지향 프로그래밍 언어를 사용하여 **호환되지 않는 유형의 시스템 간에 데이터 변화**를 사용하는 프로그래밍 기술


##  QurtySet APL
ORM에서 데이터를 검색, 필터링, 정령 및 그룹화 하는데 사용하는 

### 구문
```py
Articles.objects.all()
(model class / manager / Queryset API)
```
= SQL에서 Select * from table으로 번역

Django에서 **QuertsetAPL를 ORM을 통해 Database 보내면**  
→ Database는 ORM을 통해 Django로 **QuerySet 혹은 Instance로 반환**

### Query
데이터 베이스에서 특정한 데이터를 보여달라는 요청

### QuerySet
- 데이버베이스에서 전달 받는 객체 **목록(데이터 모음) → 순회 가능한 데이터**
- 단, **데이터 베이스가 단일 객체로 반환** 할 때 Querytset이 아닌 **Class로 반환**


## ORM Create
```bash
pip install ipython
pip install django-extensions
pip freeze > requirements.txt
```

### Django shell
django 환경 안에서 실행되는 python shell

### 객체를 만드는 3가지 방법
#### 1
```py
article = Article()
article.title = 'first'
article.content = 'djago!'

article.save()
```

#### 2. 
권장!
```py
article = Article(title='second', content='django!!')

article.save()
```

#### 3.
저장 필요 X
```py
Article.objects.create(title='third', content='django!!!')
```

## 4. ORM read
- Article.objects.all() : 전체조회
- Article.objects.get(pk=?) : 단일데이터 조회 (없으면 error)
- Article.objects.filter() : 특정조건 데이터 조회 (없으면 빈 리스트 출력)


## 5. ORM Update
```py
article = Article.objects.get(pk=1)
article.title = '수정'

article.save()
```

## 6. ORM Delete
```py
article = Article.objects.get(pk=1)
article.delete()
```
저장 별도로 필요 없음

---
참고
[QuertsetAPI](https://docs.djangoproject.com/ko/3.2/ref/models/querysets/#gt)
## Field lookups
특정 레코드에 조건을 설정하는 방법(filter(), exclude(), get()과 사용)
```py
Article.objects.filter(content__contains='dj')
```

- Article.objects.filter(pk__gt=3) : 크다
- Article.objects.filter(pk__gte=3) : 크거나 같다
- Article.objects.filter(content__contain='!') : 내용을 포함하고 있다
- Article.objects.order_by('-pk') : 내림차순
- Article.objects.order_by('?') : 랜덤으로 정렬


### Sql번역
- print(Article.objects.all().query) :
```sql
SELECT 
"articles_article"."id",
"articles_article"."title", 
"articles_article"."content", 
"articles_article"."created_at", 
"articles_article"."update_at" 
FROM "articles_article"  
```

- print(Article.objects.filter(content='django!').query)
```sql
SELECT 
"articles_article"."id", 
"articles_article"."title", 
"articles_article"."content", 
"articles_article"."created_at", 
"articles_article"."update_at" 
FROM "articles_article" 
WHERE "articles_article"."content" = django!
```



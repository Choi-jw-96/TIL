# 1

class Todo(models.Model):
    content = models.CharField(max_length=80)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=3)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True)

"""
1. 아래 할 일 생성
content : 실습 제출
priority : 5
completed : False
deadline : 오늘 날짜(년-월-일)
"""
todo = Todo(content="실습 제출", priority = "5", completed = "False", deadline=timezone.now())
todo.save()
"""
2. 아래 할 일 생성
content : 데일리 설문(오후) 제출
deadline : 오늘 날짜(년-월-일)
"""
In [1]: todo = Todo()

In [2]: todo.deadline = timezone.now()

In [3]: todo.content = '데일리 설문(오후) 제출'

In [4]: todo.save()
"""
3. 임의의 할 일 5개 생성
"""
Todo.objects.create(content="haha", deadline=timezone.now())
Todo.objects.create(content="hoho", deadline=timezone.now())
Todo.objects.create(content="huihui", priority = "4",  deadline=timezone.now())
Todo.objects.create(content="lalala", priority = "4", deadline=timezone.now())
Todo.objects.create(content="lala", deadline=timezone.now())
"""
4. pk 기준 오름차순으로 정렬한 모든 데이터 조회
"""
Todo.objects.order_by('pk')
"""
5. priority 기준 내림차순으로 정렬한 모든 데이터 조회
"""
Todo.objects.order_by('-pk')
"""
6. pk가 1인 단일 데이터의 아래 필드 조회
(pk, content, priority, deadline, created_at)
"""
todos = Todo.objects.all()
for todo in todos:
    ...:     print(todo.content)
    ...:     print(todo.priority)
    ...:     print(todo.deadline)
    ...:     print(todo.created_at)


# 2

class Newspaper(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    journalist = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)

"""
1. pk 필드가 1인 단일 데이터의 journalist 필드 조회
답 : Laney Mccullough
"""
news = Newspaper.objects.get(id=1)
news.journalist
"""
2. journalist 필드가 Laney Mccullough인 데이터 개수 조회
답 : 858
"""
news = Newspaper.objects.filter(journalist__exact='Laney Mccullough')
news.count()
"""
3. pk 필드 기준 내림차순으로 정렬한 모든 데이터 조회
답 : <QuerySet [<Newspaper: Newspaper object (10000)>, <Newspaper: Newspaper object (9999)>, ...생략
"""
Newspaper.objects.order_by('-pk')
"""
4. 필드 기준 내림차순으로 정렬한 모든 데이터 조회
답 : <QuerySet [<Newspaper: Newspaper object (4719)>, <Newspaper: Newspaper object (97)>, ...생략
"""
Newspaper.objects.order_by('-created_at')
"""
5. journalist 필드가 Britney를 포함하는 데이터 개수 조회
답 : 799
"""

"""
6. journalist 필드가 ['Britney Mahoney', 'Arianna Walls', 'Carl Short']에 속하는 데이터 개수 조회
답 : 2469
"""
news = Newspaper.objects.filter(journalist__contains='Britney Mahoney')|Newspaper.objects.filter(journalist__contains='Arianna Walls')|Newspaper.objects.filter(journalist__contains='Carl Short')
news.count()

### 창조
len(Newspaper.objects.filter(journalist__in=['Britney Mahoney', 'Arianna Walls', 'Carl Short']))

#### 홍엽
from django.db.models import Q
Newspaper.objects.filter(Q(journalist='Britney Mahoney') | Q(journalist='Arianna Walls') | Q(journalist='Carl Short')).count()
"""
7. created_at 필드가 2000-01-01 이후 데이터 개수 조회
답 : 4355
"""
Newspaper.objects.filter(created_at__gt="2000-01-01").count()
"""
8. 마지막 단일 데이터의 title, content, journalist 필드를 조회하고 아래와 같은 형식으로 출력
답
title : Teach father within million consumer baby its.
content : Then member effort want site. Radio represent yard bag fine. Congress movie ten along.
Hand receive agree science present main. Other member every.
journalist : Laney Mccullough
"""
news = Newspaper.objects.filter(id=10000).values('title', 'content', 'journalist')
for key, value in news[0].items():
    ...:     print(f'{key} : {value}')

#### 창조님
news = Newspaper.objects.all().last()
print(f'title : {news.title}')
print(f'content : {news.content}')
print(f'journalist : {news.journalist}')
"""
기타 ORM 코드 작성 후 해당 코드와 결과 코드 리뷰 시간에 공유
"""
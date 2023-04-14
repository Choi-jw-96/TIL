from django.urls import path
# 명시적 상대경로 (django 권장사항)
from . import views

# 명찰(다른 앱에서 이름이 겹쳐도 정확한 검색을 위해)
# 명찰이 붙는 순간 링크를 걸때 꼭 명찰을 붙여줘야함!
# noreversematch : url 관련 문제
app_name = 'articles'

urlpatterns = [
    path('index/', views.index, name='index'),
    # path('article/', views.index()), => 2번째 인자로 index 함수에 리턴 값이 들어가게된다
    path('dinner/', views.dinner, name='dinner'),
    path('search/', views.search, name='search'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('/<int:num>/', views.detail, name='detail'),
    path('hello/<str:name>/', views.hello, name='greeting'),
]
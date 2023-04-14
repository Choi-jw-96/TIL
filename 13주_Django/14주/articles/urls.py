from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
     path('', views.index, name = 'index'),
     path('<int:pk>/', views.detail, name='detail'),
     path('new/', views.new, name='new'),
     path('create/', views.create, name='create'),
     # 데이터 삭제에 대한 URL 패턴
     path('<int:pk>/delete/', views.delete, name='delete'),
     path('<int:pk>/edit/', views.edit, name='edit'),
     path('<int:pk>/update/', views.update, name='update'),
     
     
     # # 다양한 메서드를 사용하는 경우
     # # 데이터 조회 시 메서드 [GET]사용시
     # path('<int:pk>/', views.detail, name='detail'),
     # # 데이터 삭제 시 메서드 [DELETE] 사용시
     # path('<int:pk>/', views.delete, name='delete'),
     # # 데이터 수정 시 메서드 [PATCH] 사용시
     # path('<int:pk>/', views.update, name='update'),
]

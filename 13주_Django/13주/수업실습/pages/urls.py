from django.urls import path
# 명시적 상대경로 (django 권장사항)
from . import views

app_name = 'pages'

urlpatterns = [
    path('index/', views.index, name='index'),
]
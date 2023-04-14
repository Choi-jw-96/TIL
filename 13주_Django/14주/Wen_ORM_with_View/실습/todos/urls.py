from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:pk>', views.detail, name = 'detail'),
    path('input/', views.input, name = 'input'),
    path('create/', views.create, name ='create'),
       
]
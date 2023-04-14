from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('number-print/<int:number>/', views.number_print, name='number'),
    
]
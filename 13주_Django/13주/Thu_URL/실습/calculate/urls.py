from django.urls import path
from . import views

app_name = "calculates"

urlpatterns = [
    path('calculate/<int:number1>/<int:number2>/', views.calculate, name="calculate"),
]
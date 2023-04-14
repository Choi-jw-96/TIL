from django.urls import path
from . import views

app_name = 'albums'


urlpatterns = [
    path('', views.index, name='index'),
    path('modal', views.modal, name='modal'),
]
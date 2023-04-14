from django.urls import path
from .  import views

app_name = 'accounts'

urlpatterns = [
    path('', views.user, name='user'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
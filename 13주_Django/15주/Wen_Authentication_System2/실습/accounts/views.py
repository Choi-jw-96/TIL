from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def user(request):
  return render(request, 'accounts/user.html')


def login(request):
  if request.user.is_authenticated:
      return redirect('articles:user') 
   
  if request.method == "POST":
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
      auth_login(request, form.get_user())
      return redirect('accounts:user')
  else:
    form = AuthenticationForm()
  context = {
    'form' : form
  }
  return render(request, 'accounts/login.html', context)


def logout(request):
  auth_logout(request)
  return redirect('accounts:user')


def signup(request):
  if request.user.is_authenticated:
      return redirect('articles:user')  

  if request.method == "POST":
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      auth_login(request, user)
      return redirect("accounts:user")
  else:
      form = CustomUserCreationForm()
  context = {
    'form' : form
  }
  return render(request, 'accounts/signup.html', context)


def delete(request):
  request.user.delete()
  auth_logout(request)
  return redirect('accounts:user')


def update(request):
  if request.method == "POST":
    form = CustomUserChangeForm(request.POST, instance=request.user) 
    if form.is_valid():
      form.save()
      return redirect('accounts:user')
  else:
    form = CustomUserChangeForm(instance=request.user)
  context = {
    'form' : form
  }
  return render(request, 'accounts/update.html', context)

@login_required
def change_password(request):
  if request.method == "POST":
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      user = form.save()
      update_session_auth_hash(request, user)
      return redirect('accounts:user')
  else:
    form = PasswordChangeForm(request.user)
  context = {
    'form' : form
  }
  return render(request, 'accounts/change_password.html', context)
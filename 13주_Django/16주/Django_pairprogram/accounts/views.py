from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash
from .forms import CustomUserChangeForm, CustomUserCreationForm, CustomUserAuthenticationForm, CustomUserPasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from reviews.forms import Review


# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('reviews:index')
    if request.method == 'POST':
        form = CustomUserAuthenticationForm(request ,request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('reviews:index')
    else:
        form = CustomUserAuthenticationForm()
    context = {
        'form' : form
      }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    if request.user.is_authenticated:
       auth_logout(request)
    return redirect('reviews:index')

def signup(request):
    if request.user.is_authenticated:
        return redirect('reviews:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('reviews:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('reviews:index')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('reviews:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomUserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('reviews:index')
    else:
        form = CustomUserPasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)


@login_required
def profile(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    reviews = Review.objects.all()
    context = {
        'user': user,
        'reviews': reviews
    }
    return render(request, 'accounts/profile.html', context)
    
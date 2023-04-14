from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-pk')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': page_obj,
    }
    return render(request, 'posts/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/create.html', context)


@login_required
def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    context = {
        'post': post
    }
    return render(request, 'posts/detail.html', context)


def category(request, post_category):
    if category == '개발':
        posts = Post.objects.filter(category=post_category).order_by('-pk')
    elif category == 'CS':
        posts = Post.objects.filter(category=post_category).order_by('-pk')
    else:
        posts = Post.objects.filter(category=post_category).order_by('-pk')
    context = {
        'posts': posts,
    }
    return render(request, 'posts/category.html', context)


@login_required
def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    form = PostForm(request.POST, instance=post)
    if request.method == 'POST':       
        if form.is_valid():
            post = form.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm(instance=post)
    context = {
    'post': post,
    'form': form,
    }

    return render(request, 'posts/update.html', context)  


@login_required
def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('posts:index')    
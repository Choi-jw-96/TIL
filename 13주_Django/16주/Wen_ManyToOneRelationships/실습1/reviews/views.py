from django.shortcuts import render, redirect
from .models import Review
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, ReviewForm


# Create your views here.
def index(request):
    reviews = Review.objects.all()[::-1]
    return render(request, 'reviews/index.html', {'reviews' : reviews,})


@login_required
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews:index')
    else:
        form = ReviewForm()
    return render(request, 'reviews/create.html', {'form' : form})


def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    comments = review.comment_set.all()
    comment_form = CommentForm()
    context = {
        'review' : review,
        'comments' : comments,
        'comment_form' : comment_form,
    }
    return render(request, 'reviews/detail.html', context)


@login_required
def comment_create(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment_form.save()
        return redirect('reviews:detail', review.pk)
    context = {
        'review' :review,
        'comment_form' : comment_form
    }
    return redirect(request, 'reviews/detail.html', context)
        
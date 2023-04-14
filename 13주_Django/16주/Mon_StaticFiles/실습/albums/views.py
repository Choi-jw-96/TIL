from django.shortcuts import render, redirect
from .models import Album
from .forms import AlbumForm

# Create your views here.
def index(request):
  return render(request, 'albums/index.html')

def modal(request):
  if request.method == "POST":
    form = AlbumForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('albums:index')
  else:
    form = AlbumForm()
  context = {
    'form' : form,
  }
  return redirect('albums:index')
  # return render(request, 'albums/modal.html', context)
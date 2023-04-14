from django.shortcuts import render
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos' : todos,
    }
    return render(request, 'todos/index.html', context)


def detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo2 = todo.priority * "★"
    context = {
        'todo' : todo,
        'todo2' : todo2,
    }
    return render(request, 'todos/detail.html', context)


def input(request):
    return render(request, 'todos/input.html')


def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    priority = request.GET.get('priority')
    deadline= request.GET.get('deadline')

    todo = Todo(title=title, content=content, priority=priority, deadline=deadline)
    todo.save()

    return render(request, 'todos/create.html')
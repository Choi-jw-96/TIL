from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos' : todos
    }
    return render(request, 'todos/index.html', context)


def detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo2 = todo.priority * "★"
    context = {
        'todo' : todo,
        'todo2' : todo2
    }
    return render(request, 'todos/detail.html', context)


def new(request):
    return render(request, 'todos/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    priority = request.POST.get('priority')
    deadline = request.POST.get('deadline')
    
    todo = Todo(title=title, content=content, priority=priority, deadline=deadline)
    
    todo.save()
    
    return redirect('todos:index')


def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('todos:index')


def edit(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo' : todo,
    }
    return render(request, 'todos/edit.html', context)


def update(request, pk):
    todo = Todo.objects.get(pk=pk)

    title = request.POST.get('title')
    content = request.POST.get('content')
    priority = request.POST.get('priority')
    deadline = request.POST.get('deadline')

    todo.title = title 
    todo.content = content
    todo.priority = priority 
    todo.deadline = deadline

    todo.save()

    return redirect("todos:detail", todo.pk)


def completed(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.completed = True
    todo.save()
    return redirect('todos:index')



def uncompleted(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.completed = False
    todo.save()
    return redirect('todos:index')


def copy(request, pk):
    todo = Todo.objects.get(pk=pk)

    new_todo = Todo(
    title = todo.title,
    content = todo.content,
    priority = todo.priority,
    deadline=todo.deadline,
    )

    new_todo.save()
    
    return redirect('todos:index')



from django.shortcuts import render, redirect
from .models import AccountBook

# Create your views here.


def index(request):
    accountbooks = sorted(AccountBook.objects.all(),
                          key=lambda item: item.category)
    # accountbook = AccountBook.objects.all().order_by("category")

    context = {
        'accountbooks': accountbooks,
        # 'accountbook': accountbook
    }
    return render(request, 'accountbooks/index.html', context)


def detail(request, pk):
    accountbook = AccountBook.objects.get(pk=pk)
    context = {
        'accountbook': accountbook,
    }
    return render(request, 'accountbooks/detail.html', context)


def new(request):
    return render(request, 'accountbooks/new.html')


def create(request):
    note = request.POST.get('note')
    category = request.POST.get('category')
    amount = request.POST.get('amount')
    date = request.POST.get('date')
    description = request.POST.get('description')

    accountbook = AccountBook(
        note=note, category=category, amount=amount, date=date, description=description)

    accountbook.save()
    return redirect("accountbooks:detail", accountbook.pk)


def edit(request, pk):
    accountbook = AccountBook.objects.get(pk=pk)
    context = {
        'accountbook': accountbook,
    }
    return render(request, 'accountbooks/edit.html', context)


def update(request, pk):
    accountbook = AccountBook.objects.get(pk=pk)

    note = request.POST.get('note')
    category = request.POST.get('category')
    amount = request.POST.get('amount')
    date = request.POST.get('date')
    description = request.POST.get('description')

    accountbook.note = note
    accountbook.category = category
    accountbook.amount = amount
    accountbook.date = date
    accountbook.description = description

    accountbook.save()
    return redirect("accountbooks:detail", accountbook.pk)


def delete(request, pk):
    accountbook = AccountBook.objects.get(pk=pk)
    accountbook.delete()
    return redirect("accountbooks:index")


def copy(request, pk):
    accountbook = AccountBook.objects.get(pk=pk)

    new_accountbook = AccountBook(
        note=accountbook.note,
        category=accountbook.category,
        amount=accountbook.amount,
        date=accountbook.date,
        description=accountbook.description,
    )

    new_accountbook.save()

    return redirect("accountbooks:index")


# def category(request, category):
#     accountbooks = AccountBook.objects.filter(category=category)
#     context = {
#         'accountbooks': accountbooks
#     }
#     return render(request, "", context)

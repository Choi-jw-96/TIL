from django.shortcuts import render

# Create your views here.
# 특정 기능을 수행하는 view함수를 만듦
def index(request):
    context = {
        'name': 'Harry'
    }
    return render(request, 'articles/index.html', context)


def dinner(requst):
    foods =['볶음밥', '보쌈', '서브웨이', '햄버거']
    context = {
        'foods' : foods
    }
    return render(requst, 'articles/dinner.html', context)


def search(requst):
    return render(requst, 'articles/search.html')


def throw(requst):
    return render(requst, 'articles/throw.html')


def catch(requst):
    # print(type(requst))
    # print(dir(requst))
    # print(requst.GET.get('message'))

    data = requst.GET.get('message')
    context = {
        'data' : data,
    }
    return render(requst, 'articles/catch.html', context)


def detail(request, num):
    context = {
        'num': num,
    }
    return render(request, 'articles/detail.html', context)


def hello(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'articles/hello.html', context)
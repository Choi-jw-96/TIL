from django.shortcuts import render
import random

# Create your views here.
def today_dinner(request):
    foods = ['치킨', '삼겹살', '짜장명']
    context = {
        'food' : random.choice(foods)
    }
    return render(request, 'articles/today_dinner.html', context)

def throw(request):
    return render(request, "articles/throw.html")

def catch(request):
    data = request.GET.get('message')
    context = {
        'data' : data,
    }
    return render(request, "articles/catch.html", context)

def lotto_create(request):
    return render(request, "articles/lotto_create.html")

def lotto(request):
    lotto_num = [_ for _ in range(1, 46)]

    try:
      data = int(request.GET.get('message'))
    except:
      data = 0

    lotto_li = []
    for i in range(data):
        lotto_li.append(random.sample(lotto_num, 6))

    context = {
      'lotto_li' : lotto_li,
    }
    return render(request, "articles/lotto.html", context)

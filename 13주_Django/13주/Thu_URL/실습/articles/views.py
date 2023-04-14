from django.shortcuts import render

# Create your views here.
def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    data = request.GET.get('message')
    context = {
        'data' : data
    }
    return render(request, 'articles/catch.html', context)

def number_print(request, number):
    context = {
        'number' : number
    }
    return render(request, 'articles/number_print.html', context)
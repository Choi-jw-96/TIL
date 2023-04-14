from django.shortcuts import render

# Create your views here.
def calculate(request, number1, number2):
    sum = number1 + number2
    minus = number1 - number2
    multi = number1 * number2
    division = number1 // number2
    context = {
        'sum' : sum,
        'minus' : minus,
        'multi' : multi,
        'division' : division
    }
    return render(request, 'calculate/calculate.html', context)


from django.shortcuts import render



def bmi(request):


    height = float(request.GET.get('height', 1))
    weight = float(request.GET.get('weight', 1))

    bmi = float(weight/(height**2))

    return render(request, 'converter/bmi.html',{"bmi": bmi})


def home(request):
    return render(request, 'converter/home.html',)




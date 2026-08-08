from django.shortcuts import render
from .models import Car
from django.core.paginator import Paginator

def home(request):
    cars = Car.objects.all()
    return render(request, "index.html", context={
        'cars': cars,
    })


def detail(request, id):
    car = Car.objects.get(id=id)
    cars = Car.objects.all()
    return render(request, 'detail.html', context={
        'car':car,
        'cars':cars
    })



def catalogue(request):
    cars = Car.objects.all()
    
    paginator = Paginator(cars, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'catalogue.html', context={
        'cars': page_obj,
    })

# Create your views here.

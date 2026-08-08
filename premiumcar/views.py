from django.shortcuts import render
from .models import Car, Category
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

    categories = Category.objects.all()
        
    search = request.GET.get('search')
    category_id = request.GET.get('category')  # Получаем ID категории
    year = request.GET.get('year')
    all_cars = cars
    if search:
        cars = cars.filter(name__icontains=search)
    
    if category_id:
        cars = cars.filter(category_id=category_id)  # Фильтруем по ID категории
    
    if year:
            cars = cars.filter(year=year)
    
    paginator = Paginator(cars, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'catalogue.html', context={
        'cars': page_obj,
        'categories': categories,
        'all_cars': all_cars, 
    })

# Create your views here.

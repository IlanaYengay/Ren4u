from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Feedback, Callback, Car
from django.core.paginator import Paginator
from .forms import CarSearchForm

from .forms import CallbackForm, UserForm, CarForm
from django.contrib.auth.models import User


def index(request, car=None):
    blogs =Blog.objects.all()
    feedbacks = Feedback.objects.all()
    cars = Car.objects.all()
    if request.method == 'POST':
        form = CallbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CallbackForm()

    context = {
        'blogs': blogs,
        'feedbacks': feedbacks,
        'form': form,
        'cars': cars,
    }
    return render(request, 'blog/index.html', context)


def about(request):
    cars = Car.objects.all()
    paginator = Paginator(cars, 6)
    page = request.GET.get('page')
    cars = paginator.get_page(page)
    context = {
        'cars': cars
    }
    return render(request, 'blog/about_as.html', context)


def cars(request):
    return render(request, 'blog/car.html')


def best(request):
    cars = Car.objects.all()
    paginator = Paginator(cars, 3)
    page = request.GET.get('page')
    cars = paginator.get_page(page)
    context = {
        'cars': cars
    }
    return render(request, 'blog/best.html', context)


def blog(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/blog.html', context)


def contact(request):
    return render(request, 'blog/contact.html')


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'blog/register.html', {'form': form})


def login_views(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'blog/login.html')

def logout_view(request):
    logout(request)
    return redirect('/')


# Отображение страницы со списком автомобилей
def filter(request):
    # Обработка поиска автомобилей и формы для аренды автомобиля
    form = CarSearchForm(request.GET)
    cars_list = Car.objects.all()

    if request.method == "POST":
        messages.success(
            request,
            'Машина была успешно арендована, поздравляем! (Наши менеджера свяжутся с вами в ближайшее время)'
        )


    if form.is_valid():
        make = form.cleaned_data['make']
        model = form.cleaned_data['model']
        color = form.cleaned_data['color']
        year = form.cleaned_data['year']
        price_from = form.cleaned_data['price_from']
        price_to = form.cleaned_data['price_to']

        if price_from:
            cars_list = cars_list.filter(price__gte=price_from)
        if price_to:
            cars_list = cars_list.filter(price__lte=price_to)
        if make:
            cars_list = cars_list.filter(make=make)
        if model:
            cars_list = cars_list.filter(model__icontains=model)
        if color:
            cars_list = cars_list.filter(color=color)
        if year:
            cars_list = cars_list.filter(year=year)

    paginator = Paginator(cars_list, 6)
    page = request.GET.get('page')
    cars_list = paginator.get_page(page)

    context = {
        'form': form,
        'cars': cars_list,
    }

    # Отправка данных в шаблон и отображение страницы
    return render(request, 'blog/about.html', context)






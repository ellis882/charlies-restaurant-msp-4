from django.shortcuts import render
from .models import Menu, Category


def meals_list(request):
    meals_list = Menu.objects.all()
    categories = Category.objects.all()

    context = {
        'meals_list': meals_list,
        'categories': categories,
    }

    return render(request, 'home/index.html', context)

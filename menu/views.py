from django.shortcuts import render
from .models import Menu, Category


def menu_list(request):
    menu_list = Menu.objects.all()
    categories = Category.objects.all()

    context = {
        'menu_list': menu_list,
        'categories': categories,
    }

    return render(request, 'home/index.html', context)

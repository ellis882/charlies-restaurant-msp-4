from django.shortcuts import render


def index(request):
    """
    home page of restaurant website is index.html
    """
    context = {}
    print(True)
    return render(request, "home/index.html", context)

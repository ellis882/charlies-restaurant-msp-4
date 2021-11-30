from django.shortcuts import render


def index(request):
    context = {}
    print(True)
    return render(request, "home/index.html", context)

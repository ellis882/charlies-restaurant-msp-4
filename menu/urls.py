from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.meals_list, name="meals_list"),
]

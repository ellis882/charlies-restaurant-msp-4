from django.shortcuts import render
from django .views.generic import ListView
from .models import Table, Reservation


class TableList(ListView):
    model = Table


class ReservationList(ListView):
    model = Reservation

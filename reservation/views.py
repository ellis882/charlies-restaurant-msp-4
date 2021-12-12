from django.shortcuts import render, HttpResponse
from django .views.generic import ListView, FormView
from .models import Table, Reservation
from .forms import AvailabilityForm
from .availability import check_availability
import datetime


class TableList(ListView):
    model = Table


class ReservationList(ListView):
    model = Reservation


class ReservationView(FormView):
    form_class = AvailabilityForm
    template_name = 'reservation/availability_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        table_list = Table.objects.filter(table_size=data['table_size'])
        available_tables = []
        for table in table_list:
            if check_availability(table, data['time_start'], data['time_end']):
                available_tables.append(table)
        if len(available_tables) > 0:
            table = available_tables[0]
            reservation = Reservation.objects.create(
                user=self.request.user,
                email=email,
                phone=phone,
                table=table,
                date=datetime.date.today(),
                time_start=data['time_start'],
                time_end=data['time_end']
            )
            reservation.save()
            return HttpResponse(reservation)
        else:
            return HttpResponse('Sorry, this table_size is not available!!')

from django.shortcuts import render
from .models import Events
from .forms import EventForm
from events.models import Events


def event_reservation_form(request):
    event_form = EventForm()

    if request.method == 'POST':
        event_form = EventForm(request.POST)

        if event_form.is_valid():
            event_form.save()

    context = {'form': event_form}

    return render(request, 'events/event.html', context)

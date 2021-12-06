from django.urls import path
from . import views


app_name = 'events'

urlpatterns = [
    path('', views.event_reservation_form, name='event_reservation_form'),
]

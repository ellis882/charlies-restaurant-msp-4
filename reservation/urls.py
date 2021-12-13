from django.urls import path
from .views import TableList, ReservationList, ReservationView, CancelReservationView

app_name = 'reservation'

urlpatterns = [
    path('table_list/', TableList.as_view(), name='TableList'),
    path('reservation_list/', ReservationList.as_view(),
         name='ReservationList'),
    path('book_a_table/', ReservationView.as_view(),
         name='ReservationView'),
    path('reservation/cancel/<pk>', CancelReservationView.as_view(),
         name='CancelReservationView'),
]

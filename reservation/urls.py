from django.urls import path
from .views import ReservationList, ReservationView
from .views import CancelReservationView, TableDetailView

app_name = 'reservation'

urlpatterns = [    
    path('reservation_list/', ReservationList.as_view(),
         name='ReservationList'),
    path('book_a_table/', ReservationView.as_view(),
         name='ReservationView'),
    path('reservation/cancel/<pk>', CancelReservationView.as_view(),
         name='CancelReservationView'),
    path('table/<table_size>', TableDetailView.as_view(), name='TableDetailView'),    
]

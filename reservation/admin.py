from django.contrib import admin
from .models import Table, Reservation


class ReservationAdmin(admin.ModelAdmin):
    list_display = ['user', 'table',
                    'date_time_start']
    search_fields = ['user', 'date_time_start']
    list_filter = ['user', 'date_time_start']


class TableAdmin(admin.ModelAdmin):
    list_display = ['table_nr', 'table_size']


admin.site.register(Table, TableAdmin)
admin.site.register(Reservation, ReservationAdmin)

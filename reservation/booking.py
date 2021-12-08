from datetime import timedelta
from django.db.models import Sum
from .models import Table, Reservation


def book_a_table(table, booking_date_time, nr_of_people, minutes_slot=90):
    """
    This method uses get_first_table_available to get the first table
    available, then it creates a Reservation on the database.
    """
    table = get_first_table_available(table, booking_date_time, nr_of_people,
                                      minutes_slot)

    if table:
        delta = timedelta(seconds=60*minutes_slot)
        reservation = Reservation(table=table, nr_of_people=nr_of_people,
                                  reservation_date_time_start=reservation_date_time,
                                  reservation_date_time_end=reservation_date_time + delta)
        reservation.save()
        return {'reservation': reservation.id, 'table': table.id}
    else:
        return None


def get_first_table_available(table, reservation_date_time, nr_of_people,
                              minutes_slot=90):
    """
    This method returns the first available table, given a specific number of
    people and a reservation date/time.
    """
    # I make sure to check if the tables are not already booked within the time
    # slot required by the new reservation
    delta = timedelta(seconds=60*minutes_slot)
    l_bound_time = reservation_date_time
    u_bound_time = reservation_date_time + delta

    tables_reservation_ids = []

    # Exclude tables which start and end reservation date includes requested
    # initial reservation date_time
    tables_reservation = Reservation.objects.filter(table__nr=table,
                         reservation_date_time_start__lt=l_bound_time,
                         reservation_date_time_end__gt=l_bound_time).values('table')
    tables_reservation_ids_temp = [x['table'] for x in tables_reservation]
    tables_reservation_ids = tables_reservation_ids + tables_reservation_ids_temp

    # Exclude tables which start and end reservation date includes requested
    # ending reservation date_time
    tables_reservation = Reservation.objects.filter(
        reservation_date_time_start__lt=u_bound_time,
        reservation_date_time_end__gt=u_bound_time).values('table')
    tables_reservation_ids_temp = [x['table'] for x in tables_reservation]
    tables_reservation_ids = tables_reservation_ids + tables_reservation_ids_temp

    # Exclude tables which reservation slots is inside requested reservation
    # slot
    tables_reservation = Reservation.objects.filter(
        reservation_date_time_start__gt=l_bound_time,
        reservation_date_time_end__lt=u_bound_time).values('table')
    tables_reservation_ids_temp = [x['table'] for x in tables_reservation]
    tables_reservation_ids = tables_reservation_ids + tables_reservation_ids_temp

    # Exclude tables which include requested reservation slot
    tables_reservation = Reservation.objects.filter(
        reservation_date_time_start__lt=l_bound_time,
        reservation_date_time_end__gt=u_bound_time).values('table')
    tables_reservation_ids_temp = [x['table'] for x in tables_reservation]
    tables_reservation_ids = tables_reservation_ids + tables_reservation_ids_temp

    # Then I get a list of all the tables, of the needed size, available and
    # I exclude the previous list of unavailable tables. I order the list from
    # the smaller table to the bigger one and I return the first, smaller one,
    # available.
    tables = Table.objects.filter(table_nr=table_nr,
        table__opening_time__lte=reservation_date_time.hour,
        table__closing_time__gte=reservation_date_time.hour+(minutes_slot / float(60)),
        table_size__gte=nr_of_people).exclude(id__in=tables_reservation_ids).order_by('table_size')

    if tables.count() == 0:
        return None
    else:
        return tables[0]


def get_expected_diners(table_nr, reservation_date):
    """
    Return the expected number of diners for a specific date.
    """
    diners = Reservation.objects.filter(
        table__table_nr=table_nr,
        reservation_date_time_start__year=reservation_date.year,
        reservation_date_time_start__month=reservation_date.month,
        reservation_date_time_start__day=reservation_date.day).aggregate(Sum('nr_of_people'))
    return diners['nr_of_people__sum']

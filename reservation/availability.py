from .models import Reservation


def check_availability(table, date_time_start, date_time_end):
    avail_list = []
    reservation_list = Reservation.objects.filter(table=table)
    for reservation in reservation_list:
        if reservation.date_time_start > date_time_end or reservation.date_time_end < date_time_start:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)

from .models import Reservation


def check_availability(table, time_start, time_end):
    avail_list = []
    reservation_list = Reservation.objects.filter(table=table)
    for reservation in reservation_list:
        if reservation.time_start > time_end or reservation.time_end < time_start:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)

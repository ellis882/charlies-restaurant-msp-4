from .models import Reservation


def check_availability(table, date, time_start, time_end):
    avail_list = []
    reservation_list = Reservation.objects.filter(table=table, date=date)
    for reservation in reservation_list:
        if reservation.time_start > time_end or reservation.time_end < time_start:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)

from .models import Reservation


def check_availability(table, date, time_start, time_end):
    avail_list = []
    reservation_list = Reservation.objects.filter(table=table)
    for reservation in reservation_list:
        if reservation.time_start + date > time_end + date or reservation.time_end + date < time_start + date:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)

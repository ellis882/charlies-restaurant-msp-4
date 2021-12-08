from django.db import models
from django.conf import settings


class Table(models.Model):
    table_nr = models.IntegerField()
    table_size = models.IntegerField()
    opening_time = models.IntegerField(null=True)
    closing_time = models.IntegerField(null=True)

    def __str__(self):
        return str(self.table_nr)


class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    nr_of_people = models.IntegerField()
    reservation_date_time_start = models.DateTimeField()
    reservation_date_time_end = models.DateTimeField()

    def __str__(self):
        return str(self.user)

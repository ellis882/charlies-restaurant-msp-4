from django.db import models
from django.conf import settings
from datetime import datetime


class Customer(models.Model):
    email = models.EmailField()
    phone = models.IntegerField()

    def __str__(self):
        return str(self.email)


class Table(models.Model):
    table_nr = models.IntegerField()
    TABLE_SIZE_LIST = (
        ('two persons', 'TWO PERSONS'),
        ('four persons', 'FOUR PERSONS'),
        ('six persons', 'SIX PERSONS'),
        ('eight persons', 'EIGHT PERSONS'),
    )
    table_size = models.CharField(max_length=15, choices=TABLE_SIZE_LIST)

    def __str__(self):
        return f'tablenumber {self.table_nr} for {self.table_size}'


class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)     
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)
    time_start = models.TimeField(default=datetime.now)
    time_end = models.TimeField(default=datetime.now)

    def __str__(self):
        return f'{self.user} has booked {self.table} at {self.date} from {self.time_start} until {self.time_end}'

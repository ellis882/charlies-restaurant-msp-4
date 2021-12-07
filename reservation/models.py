from django.db import models


class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField(blank=True)
    number_of_persons = models.IntegerField()
    Date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return str(self.name)

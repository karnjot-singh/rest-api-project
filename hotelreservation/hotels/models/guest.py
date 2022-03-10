from django.db import models
from .reservation import Reservation

class Guest(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1)

    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name
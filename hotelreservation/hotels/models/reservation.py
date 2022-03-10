from django.db import models
from .hotel import Hotel

class Reservation(models.Model):
    id = models.AutoField(primary_key=True)

    confirmation_number = models.CharField(max_length=10);

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=False)

    check_in = models.DateField()
    check_out = models.DateField()


    def __str__(self):
        return self.confirmation_number
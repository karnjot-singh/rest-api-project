from django.db import models

class Hotel(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=500)
    availability = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
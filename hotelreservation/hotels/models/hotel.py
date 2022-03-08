from django.db import models
from django.core.validators import RegexValidator

class Hotel(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=500)
    availability = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=21, validators=[
            RegexValidator(regex='^[0-9]{10,20}$', message='Ensure this field has 10-20 digits.')])
    city = models.CharField(max_length=30)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
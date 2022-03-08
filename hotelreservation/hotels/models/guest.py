from django.db import models

class Guest(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=50, unique=True)
    gender = models.CharField(max_length=1)

    def __str__(self):
        return self.name
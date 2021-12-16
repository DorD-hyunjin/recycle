from django.db import models
from django.utils import timezone


class Point(models.Model):
    phone_number = models.CharField(primary_key=True, max_length=15)
    point = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.phone_number




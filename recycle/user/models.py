from django.db import models
from django.utils import timezone


class Point(models.Model):
    phone_number = models.CharField(primary_key=True, max_length=15)
    point = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.phone_number

# class User(models.Model):
#     objects = models.Manager()
#
#     phone_number = models.CharField(primary_key=True, max_length=15)
#     recent_point = models.IntegerField(default=0)
#     sum_points = models.IntegerField(default=0)
#     count = models.IntegerField(default=1)
#     recent_date = models.DateTimeField(default=timezone.now)
#
#     def __str__(self):
#         return self.phone_number
#
#
# class Record(models.Model):
#     objects = models.Manager()
#
#     ID = models.AutoField(primary_key=True)
#     phone_number = models.ForeignKey('User', on_delete=models.RESTRICT)
#     point = models.IntegerField(default=0)
#     sum_points = models.IntegerField(default=0)
#     count = models.IntegerField(default=0)
#     date = models.DateTimeField(default=timezone.now)
#
#     def __str__(self):
#         return self.phone_number



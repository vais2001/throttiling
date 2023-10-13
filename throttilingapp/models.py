from django.db import models
from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    phone_number=models.IntegerField()
    city = models.CharField(max_length=100)

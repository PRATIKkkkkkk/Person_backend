from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    email = models.EmailField()
    contact = models.IntegerField()
    address = models.TextField()
    pincode = models.IntegerField()
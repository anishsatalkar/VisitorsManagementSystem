from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Visitor(models.Model):
    first_name = models.CharField(max_length=70)
    middle_name = models.CharField(max_length=70, blank=True, null=True)
    last_name = models.CharField(max_length=70)

    email = models.EmailField()
    mobile = models.CharField(max_length=15, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    organisation = models.CharField(max_length=250, blank=True, null=True)
    university = models.CharField(max_length=250, blank=True, null=True)
    designation = models.CharField(max_length=100)

    purpose_of_visit = models.CharField(max_length=500, null=True, blank=True)
    date_time_of_entry = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Address(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    building = models.CharField(max_length=50, blank=True, null=True)
    pin_code = models.PositiveIntegerField()
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.building + " " + self.street + " " + self.city + " " + self.state + " " + self.country + " " + str(
            self.pin_code)

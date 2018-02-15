from django.db import models


class Address(models.Model):
    building = models.CharField(max_length=50,blank=True,null=True)
    pin_code = models.PositiveIntegerField()
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.building + " " + str(self.pin_code) + " " + self.street + " " + self.city + " " + self.state + " " + self.country


class Visitor(models.Model):
    first_name = models.CharField(max_length=70)
    middle_name = models.CharField(max_length=70 ,blank=True, null=True)
    last_name = models.CharField(max_length=70)

    email = models.EmailField()
    mobile = models.BigIntegerField()
    phone = models.BigIntegerField(null=True , blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE,blank=True,null=True)

    organisation = models.CharField(max_length=250, blank=True, null=True)
    university = models.CharField(max_length=250, blank=True, null=True)
    designation = models.CharField(max_length=100)

    purpose_of_visit = models.CharField(max_length=500, null=True , blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Log(models.Model):
    visitor = models.ForeignKey(Visitor)
    date_time_of_entry = models.DateTimeField()
    date_time_of_exit = models.DateTimeField()

    def log_entry(self, visitor , date_time_of_entry, date_time_of_exit):
        self.visitor = visitor
        self.date_time_of_entry = date_time_of_entry
        self.date_time_of_exit = date_time_of_exit
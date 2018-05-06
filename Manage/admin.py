from django.contrib import admin

# Register your models here.
from Manage.models import Visitor, Address

admin.site.register(Visitor)
admin.site.register(Address)
"""These model classes represent database tables
that will be extended to other functionality and also 
store user data"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#A = dateformat.format(timezone.now(), 'Y-m-d H:i:s')

class Manager(models.Model):
    id = models.IntegerField(null = False, primary_key = True)
    name = models.CharField(max_length = 30, null = True)


# Create your models here.
class Employee(models.Model):
    id = models.IntegerField(primary_key = True)
    managerId = models.ForeignKey(Manager, on_delete = models.CASCADE, null = True, blank = True)
    userId = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    username = models.CharField(max_length = 30, null = False)
    comment = models.TextField(null = True, blank = False)
    complete = models.BooleanField(default = False)
    written = models.DateTimeField(default = timezone.now())


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['complete']


class Sessions(models.Model):
    id = models.IntegerField(primary_key = True, null = False)
    userId = models.ForeignKey(Employee, on_delete = models.CASCADE, null = True )
    duration = models.DecimalField(null = False, max_digits = 20, decimal_places = 20)



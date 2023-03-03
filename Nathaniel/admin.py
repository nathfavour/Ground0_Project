"""This is where the database tables (or referred to
as models in django) are set to be displayed in the admin page"""


from django.contrib import admin
from .models import Sessions, Employee

# Register your models here.

admin.site.register(Sessions)
admin.site.register(Employee)


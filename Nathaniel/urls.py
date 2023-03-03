"""this file makes it possijle for us to locate 
different views by the urlpatterns configured here"""


from django.urls import path
from . import views
from .views import register

urlpatterns = [
    path('', register.as_view(), name = 'register'),

]



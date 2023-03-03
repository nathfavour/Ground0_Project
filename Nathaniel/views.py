"""This file configures the views that will be seen
when the pages load"""


from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse


class register(FormView):
    template_name = 'Nathaniel/register.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(register, self).form_valid(form)

    def get_success_url(request):
        return HttpResponse('<h1> Thank you for Registering!!!</h1>')




from django.views.generic import CreateView
from accounts.forms import UserCreateForm
from django.urls import reverse_lazy

# Create your views here.


class Signup(CreateView):
    form_class = UserCreateForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
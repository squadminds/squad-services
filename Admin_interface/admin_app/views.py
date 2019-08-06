from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.models import User
# Create your views here.


@user_passes_test(lambda u: u.is_superuser)
def admin_home(request):
    return render(request, 'admin_app/admin_welcome_page.html')


class UserListView(UserPassesTestMixin, ListView):
    model = User
    template_name = 'admin_app/user_list.html'
    context_object_name = 'users'

    def test_func(self):
        return self.request.user.is_superuser


class UserDetailView(UserPassesTestMixin, DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'admin_app/user_detail.html'

    def test_func(self):
        return self.request.user.is_superuser

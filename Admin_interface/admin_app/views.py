from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
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


@user_passes_test(lambda u: u.is_superuser)
def delete_user(request, pk):
    """
    Delete a single Checked User
    :param request:
    :param pk:
    :return:
    """
    user = User.objects.get(pk=pk)
    user.delete()
    return reverse_lazy('admin:user_list')

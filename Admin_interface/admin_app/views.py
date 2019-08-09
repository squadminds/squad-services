from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from accounts.forms import UserCreateForm
from django.urls import reverse_lazy
from admin_app.forms import PasswordChangeForm


# Create your views here


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
    context_object_name = 'this_user'
    template_name = 'admin_app/user_detail.html'

    def test_func(self):
        return self.request.user.is_superuser


class UserDeleteView(UserPassesTestMixin, DeleteView):
    success_url = reverse_lazy('admin:user_list')
    model = User

    def test_func(self):
        return self.request.user.is_superuser


class UserAdd(UserPassesTestMixin, CreateView):
    form_class = UserCreateForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('admin:user_list')

    def test_func(self):
        return self.request.user.is_superuser


@user_passes_test(lambda u: u.is_superuser)
def delete_user(request):
    if request.method == 'POST':
        User.objects.filter(pk__in=request.POST.getlist('checkbox_value')).delete()
    return redirect('admin:user_list')


class UserUpdate(UserPassesTestMixin, UpdateView):
    models = User
    fields = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser',
              'user_permissions')

    def get_object(self, queryset=None):
        obj = User.objects.get(pk=self.kwargs['pk'])
        self.success_url = reverse_lazy('admin:user_detail', kwargs={'pk': obj.pk})
        return obj

    def test_func(self):
        return self.request.user.is_superuser


class ChangePassword(UserPassesTestMixin, PasswordChangeView):

    def test_func(self):
        return self.request.user.is_superuser


class PasswordChange(UserPassesTestMixin, UpdateView):

    form_class = PasswordChangeForm
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('login')

    def get_object(self, queryset=None):
        return self.request.user

    def test_func(self):
        return self.request.user.is_superuser


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })
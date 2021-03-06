from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User, Permission
from django.contrib.auth.views import PasswordChangeView
from accounts.forms import UserCreateForm
from django.urls import reverse_lazy
from admin_app.forms import MyUserUpdateForm
from catalogue.models import Product
from category.models import Category

# Create your views here


@user_passes_test(lambda u: u.is_superuser)
def admin_home(request):
    return render(request, 'admin_app/admin_home.html')


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
    form_class = MyUserUpdateForm

    def get_object(self, queryset=None):
        obj = User.objects.get(pk=self.kwargs['pk'])
        self.success_url = reverse_lazy('admin:user_detail', kwargs={'pk': obj.pk})
        return obj

    def test_func(self):
        return self.request.user.is_superuser


class CategoryListView(UserPassesTestMixin, ListView):
    model = Category
    template_name = 'admin_app/category_list.html'
    context_object_name = 'category'

    def test_func(self):
        return self.request.user.is_superuser


class CategoryAdd(UserPassesTestMixin, CreateView):
    model = Category
    fields = '__all__'
    template_name = 'admin_app/create_category.html'
    success_url = reverse_lazy('admin:category_list')

    def test_func(self):
        return self.request.user.is_superuser


class CategoryDetailUpdate(UserPassesTestMixin, UpdateView):
    model = Category
    fields = '__all__'
    context_object_name = 'category'
    template_name = 'admin_app/update_category.html'

    def get_object(self, queryset=None):
        obj = Category.objects.get(pk=self.kwargs['pk'])
        self.success_url = reverse_lazy('admin:category_list')
        return obj

    def test_func(self):
        return self.request.user.is_superuser


class ProductListView(UserPassesTestMixin, ListView):
    model = Product
    template_name = 'admin_app/product_list.html'
    context_object_name = 'products'

    def test_func(self):
        return self.request.user.is_superuser


class ProductAdd(UserPassesTestMixin, CreateView):
    model = Product
    fields = '__all__'
    template_name = 'admin_app/create_product.html'
    success_url = reverse_lazy('admin:product_list')

    def test_func(self):
        return self.request.user.is_superuser


class ProductDetailUpdate(UserPassesTestMixin, UpdateView):
    model = Product
    fields = '__all__'
    context_object_name = 'product'
    template_name = 'admin_app/update_product.html'

    def get_object(self, queryset=None):
        obj = Product.objects.get(pk=self.kwargs['pk'])
        self.success_url = reverse_lazy('admin:product_list')
        return obj

    def test_func(self):
        return self.request.user.is_superuser

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from admin_app.forms import MyUserUpdateForm
from accounts.forms import UserCreateForm
from catalogue.models import Product
from category.models import Category
# Create your views here


@user_passes_test(lambda u: u.is_superuser)
def admin_home(request):
    return render(request, 'admin_app/admin_home.html')


@user_passes_test(lambda u: u.is_superuser)
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('admin:admin_home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'auth/password_change.html', {
        'form': form
    })


# ___________________________ User's Views Starts Here ____________________________#


class UserListView(UserPassesTestMixin, ListView):
    model = User
    template_name = 'admin_app/user_list.html'
    context_object_name = 'users'
    def get_queryset(self):
        queryset = User.objects.all()
        if self.request.GET.get('sort_by'):
            queryset = User.objects.order_by(self.request.GET.get('sort_by'))
        return queryset

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

# ____________________ Models Views Starts Here______________________________#


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

# _______________________Group Views Start from Here ___________________________#


class GroupListView(UserPassesTestMixin, ListView):
    model = User
    template_name = 'admin_app/group_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        group_name = (self.kwargs['group'])
        if group_name == 'admin':
            context['user_list']= User.objects.filter(is_superuser=True, is_staff=True)
        elif group_name == 'staff':
            context['user_list'] = User.objects.filter(is_staff=True)
        else:
            context['user_list'] = User.objects.filter(is_superuser=False, is_staff=False)
        return context

    def test_func(self):
        return self.request.user.is_superuser
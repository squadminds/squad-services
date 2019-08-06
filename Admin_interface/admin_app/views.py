from django.shortcuts import render,redirect
from django.contrib.auth.decorators import user_passes_test
from admin_app.forms import LoginForm
from django.contrib.auth import login, authenticate, logout
from django.forms import ValidationError

# Create your views here.


@user_passes_test(lambda u: u.is_superuser)
def admin_home(request):
    return render(request, 'admin_welcome_page.html')


def login_admin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user.is_superuser:
                login(request, user)
    else:
        form = LoginForm()
    return render(request,'admin_login_page.html', {'form': form})


def admin_logout(request):
    logout(request)
    return redirect('home')
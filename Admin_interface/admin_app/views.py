from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Create your views here.


@user_passes_test(lambda u: u.is_superuser)
def admin_home(request):
    return render(request, 'admin_app/admin_welcome_page.html')
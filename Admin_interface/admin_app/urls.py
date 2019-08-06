from django.urls import path
from admin_app import views


app_name = 'admin'

urlpatterns = [
    path('home/', views.admin_home, name='admin_home'),
]
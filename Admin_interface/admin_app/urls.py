from django.urls import path
from admin_app import views


urlpatterns = [
    path('home/', views.admin_home, name='admin_home'),
    path('login/', views.login_admin, name='admin_login'),
    path('logout/', views.admin_logout, name='admin_logout'),
]
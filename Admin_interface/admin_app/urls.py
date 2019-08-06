from django.urls import path
from admin_app import views


app_name = 'admin'

urlpatterns = [
    path('home/', views.admin_home, name='admin_home'),
    path('users/', views.UserListView.as_view(), name= 'user_list'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name= 'user_detail'),
]
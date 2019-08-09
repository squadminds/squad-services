from django.urls import path
from admin_app import views


app_name = 'admin'

urlpatterns = [
    path('home/', views.admin_home, name='admin_home'),
    path('users/', views.UserListView.as_view(), name= 'user_list'),
    path('user/add/', views.UserAdd.as_view(), name='add_user'),
    path('user/<int:pk>/', views.UserDetailView.as_view(), name= 'user_detail'),
    path('user/delete/<int:pk>', views.UserDeleteView.as_view(), name='delete_user'),
    path('user/delete/', views.delete_user, name='delete_selected_user'),
    path('user/update/<int:pk>', views.UserUpdate.as_view(), name='update_user')
]
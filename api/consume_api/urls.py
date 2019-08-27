from django.urls import path
from . import views

urlpatterns = [
    path('users/list/', views.show_users_list, name='users_list'),
    path('choices/', views.show_choices, name='choices'),
]
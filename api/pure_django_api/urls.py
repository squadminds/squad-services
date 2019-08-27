from django.urls import path, include
from . import views

urlpatterns = [
    path("polls/list", views.polls_list, name="polls_list"),
    path("poll/<int:pk>/detail/", views.polls_detail, name="polls_detail"),
]
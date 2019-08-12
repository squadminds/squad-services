from django.urls import path
from . import views

app_name = 'category'

urlpatterns=[
    path('', views.ServiceList.as_view(), name='service_list'),
    path('<slug:slug>/',views.ServiceDetailView.as_view(),name='service_detail'),
]
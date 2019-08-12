from django.urls import path
from .models import Category
from .views import CategoryDetailView

app_name='category'

urlpatterns=[
    path('<slug:slug>',CategoryDetailView.as_view(),name='category_detail'),
]
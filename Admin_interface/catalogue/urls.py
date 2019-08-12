from django.urls import path
from .views import ProductDetailView

app_name='catalogue'

urlpatterns=[
    path('<slug:slug>',ProductDetailView.as_view(),name='product_detail'),
]
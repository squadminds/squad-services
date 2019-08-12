from django.shortcuts import render
from .models import Product
from django.views.generic import DetailView

# Create your views here.
class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'catalogue/product_detail.html'
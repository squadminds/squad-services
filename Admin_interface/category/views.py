from django.shortcuts import render
from django.views.generic import DetailView,ListView
from .models import Category

# Create your views here.
class CategoryDetailView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'category/category_detail.html'

class HomeView(ListView):
    model = Category
    context_object_name = 'category'
    template_name = 'home.html'
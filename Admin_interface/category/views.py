from django.views.generic import DetailView,ListView
from .models import Category

# Create your views here.
class ServiceDetailView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'category/category_detail.html'


class ServiceList(ListView):
    model = Category
    context_object_name = 'services'
    template_name = 'category/service_list.html'
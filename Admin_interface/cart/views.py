from django.shortcuts import render,get_object_or_404,redirect
from category.models import Category
from catalogue.models import Product
from .cart import Cart


def add(request,id):
    product=get_object_or_404(Product,id=id)
    cart=Cart(request)
    cart.add(product)
    return redirect('cart:show')

def remove(request,id):
    cart=Cart(request)
    product=get_object_or_404(Product,id=id)
    cart.remove(product)
    return redirect('cart:show')

def show(request):
    cart=Cart(request)
    return render(request,'cart/show_cart.html',{'cart':cart})

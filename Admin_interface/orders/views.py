from django.shortcuts import render,redirect,get_object_or_404
from orders.forms import OrderForm
from orders.models import Order,OrderItem
from cart.cart import Cart

def checkout(request):
        cart = Cart(request)
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                order = form.save()
                for item in cart:
                    OrderItem.objects.create(order=order,
                                             product=item['product'],
                                             price=item['price'],
                                             quantity=item['quantity'])

                cart.clear()
                return render(request,
                              'orders/thankyou.html',
                              {'order': order})

        else:
            form = OrderForm()
        return render(request,
                      'orders/order_create.html',
                      {'cart': cart, 'form': form})



from catalogue.models import Product
from django.conf import settings
from decimal import Decimal


class Cart:

    def __init__(self,request):

        self.session=request.session
        cart=self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart=self.session[settings.CART_SESSION_ID]={}

        self.cart=cart

    def add(self,product,quantity=1,update=False):
        product_id=str(product.id)

        if product_id not in self.cart:
            self.cart[product_id]={
                'price':str(product.price),
                'quantity':0
            }

        if update:
            self.cart[product_id]['quantity']=quantity
                # because drop down menu/form field input changes the total quantity
        else:
            self.cart[product_id]['quantity']+=quantity
                #simply means add 1 to quantity

        self.save()
        #defined below

    def remove(self,product):
        if str(product.id) in self.cart:
            del self.cart[str(product.id)]
            self.save()

    def save(self):
        self.session.modified=True

    def __iter__(self):
        product_ids=self.cart.keys()
        products=Product.objects.filter(id__in=product_ids)
        cart=self.cart.copy()

        for product_object in products:
            cart[str(product_object.id)]['product']=product_object

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item


    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def total_price(self):
        return sum(Decimal(item['price'])*item['quantity'] for item in
                                                    self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

from django.db import models
from django.core.validators import RegexValidator
from catalogue.models import Product
from django.core.validators import MaxValueValidator


class Order(models.Model):
    valid=r'[a-zA-Z\s]+$'
    name=models.CharField(max_length=20,
                          validators=[RegexValidator(valid)])
    email=models.EmailField()
    phone=models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)])
    address=models.TextField()
    pincode=models.PositiveIntegerField(validators=[MaxValueValidator(999999)])
    city=models.CharField(max_length=128)
    state=models.CharField(max_length=128)
    created_on=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_on=models.DateTimeField(auto_now=True,auto_now_add=False)
    paid=models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return 'Order	{}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order=models.ForeignKey(Order,related_name='item',on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='order_items')
    price=models.DecimalField(max_digits=12,decimal_places=2)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.id

    def get_cost(self):
        return self.price * self.quantity





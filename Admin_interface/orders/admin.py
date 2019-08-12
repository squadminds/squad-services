from django.contrib import admin
from orders.models import Order, OrderItem


#No Idea. This is copied from a tutorial
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email','phone',
                    'address', 'pincode', 'city', 'paid',
                    'created_on', 'updated_on']
    list_filter = ['paid', 'created_on', 'updated_on']
    inlines = [OrderItemInline]



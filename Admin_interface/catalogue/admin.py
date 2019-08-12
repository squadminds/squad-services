from django.contrib import admin
from catalogue.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','slug','price','available','created_on','updated_on']
    list_filter	=['available','created_on','updated_on']
    list_editable=['price', 'available']
    prepopulated_fields	={'slug': ('name',)}
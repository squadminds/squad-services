from django.contrib import admin
from category.models import Category


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','slug','available','created_on','updated_on']
    list_filter	=['available','created_on','updated_on']
    list_editable=['available',]
    prepopulated_fields	={'slug': ('name',)}
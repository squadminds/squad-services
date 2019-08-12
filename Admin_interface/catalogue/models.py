from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    category=models.ForeignKey(Category,related_name='products',
                               on_delete=models.CASCADE)
    name=models.CharField(max_length=128, db_index=True,unique=True)
    stock=models.IntegerField()
    available=models.BooleanField()
    created_on=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_on=models.DateTimeField(auto_now=True,auto_now_add=False)
    price=models.DecimalField(decimal_places=2,max_digits=12)
    slug=models.SlugField(db_index=True,unique=True)
    image=models.ImageField(upload_to='products/%y/%m/%d/', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalogue:product_detail',kwargs={'slug':self.slug})

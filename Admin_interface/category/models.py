from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=128,db_index=True,unique=True)
    slug=models.SlugField(db_index=True,unique=True)
    created_on=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_on=models.DateTimeField(auto_now=True,auto_now_add=False)
    available=models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cart:category_detail',kwargs={'slug':self.slug})
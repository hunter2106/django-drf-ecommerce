from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.

class Brand(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(MPTTModel):
    name=models.CharField(max_length=100)   
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True) 

    class MPTTMeta:
        order_insertion_by = ['name']
    
    class Meta:                 # compound index
        indexes = [
            models.Index(fields=['name', 'parent']),
        ]

    def __str__(self):
        return self.name
        


class Product(models.Model):
    name=models.CharField(max_length=100) 
    desc=models.TextField()
    is_digital=models.BooleanField(default=False)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    category=TreeForeignKey('Category', on_delete=models.PROTECT) 
    is_active=models.BooleanField(default=False)  

    def __str__(self):
        return self.name
    

class ProductLine(models.Model):
       price=models.DecimalField(decimal_places=2,max_digits=7) 
       stock_qty=models.IntegerField()
       sku=models.CharField(max_length=100, unique=True)        # unique index
       product=models.ForeignKey(Product,on_delete=models.CASCADE)
       is_active=models.BooleanField(default=False)

       class Meta:
        indexes = [
            models.Index(fields=['-price'], name='idx_price_desc'),         # ordered index
            models.Index(fields=['sku'], name='idx_active_sku', condition=models.Q(is_active=True))     # partial index
        ]

       def __str__(self):
          return self.sku


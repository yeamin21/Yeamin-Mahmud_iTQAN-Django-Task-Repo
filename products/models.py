from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/categories/')
    
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.ImageField(upload_to='images/products/')
    description = models.TextField(null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name

class ProductViewCount(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)
    
@receiver(post_save, sender=Product)
def add_view_count(sender, instance, created, **kwargs):
    if created:
        ProductViewCount.objects.create(product=instance)
        return ProductViewCount
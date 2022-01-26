from itertools import product
from django.contrib import admin
from .models import Product, Category, ProductViewCount
from django.db.models import F


class ProductInline(admin.TabularInline):
    model = Product
    extra = 0
class CategoryAdmin(admin.ModelAdmin):
    inlines=[ProductInline]

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','category','view_count']
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = Product.objects.annotate(view_count =F('productviewcount__value')).order_by('-view_count')
        return queryset
    
    @admin.display(empty_value=0)
    def view_count(self, obj):
         return ProductViewCount.objects.get(product=obj).value
    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
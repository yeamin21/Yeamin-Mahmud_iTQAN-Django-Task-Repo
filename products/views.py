from .models import Product, Category, ProductViewCount
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class CategoryListView(LoginRequiredMixin, generic.ListView):
    model = Category
    template_name = 'products/category_list.html'
    
class ProductListView(generic.ListView):
    model = Product

class CategoryDetailView(LoginRequiredMixin,generic.DetailView):
    model = Category
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(category_id = self.kwargs['pk'])
        return context

class ProductDetailView(LoginRequiredMixin,generic.DetailView):
    model = Product
    
    def get(self, request, *args, **kwargs):
        product_view = ProductViewCount.objects.get(product=self.kwargs['pk'])
        product_view.value += 1
        product_view.save()
        return super().get(request, *args, **kwargs)
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["view_count"] = ProductViewCount.objects.get(product_id = self.kwargs['pk']).value
    #     return context
 
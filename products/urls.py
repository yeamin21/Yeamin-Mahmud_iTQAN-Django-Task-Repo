import imp
from importlib.resources import path


from .views import CategoryDetailView, ProductListView,CategoryListView,ProductDetailView
from django.urls import path
app_name = 'products'
urlpatterns = [  
    path('',CategoryListView.as_view(), name='categories'),
    path('products/',ProductListView.as_view(), name='products'),
    path('category/<int:pk>/',CategoryDetailView.as_view(), name='category-details'),
    path('products/<int:pk>/',ProductDetailView.as_view(), name='product-details'),
]

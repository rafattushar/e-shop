from django.shortcuts import render
from django.views import generic

from .models import Product
from category.models import Category

# Create your views here.

class ProductList(generic.ListView):
    model = Product
    template_name = 'product/product_list.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.all().order_by('created_at')


class ProductDetail(generic.DetailView):
    model = Product
    template_name = 'product/product_detail.html'

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(pk=self.kwargs.get('pk'))


class CategoryProduct(generic.ListView):
    model = Product
  
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(product_cat__slug=self.kwargs.get('slug'))
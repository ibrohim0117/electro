from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from product.models import ProductCategory, Product


class CategoryView(ListView):
    model = ProductCategory
    queryset = ProductCategory.objects.all()
    context_object_name = 'product'
    template_name = 'base.html'


class ProductIndexView(ListView):
    model = Product
    template_name = 'index.html'
    queryset = Product.objects.all()
    context_object_name = 'product'

    # def get(self, request):
    #     if request.GET:
    #         product = Product.objects.filter(title=request.GET['search'])
    #         return render(request, 'index.html', {'product': product})
    #     else:
    #         product = Product.objects.all()
    #         return render(request, 'index.html', {'product': product})

    # def post(self, request):
    #     product = Product.objects.filter(title=request.POST.get['search'])
    #     return render(request, 'index.html', {'product': product})


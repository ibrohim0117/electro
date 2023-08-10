from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, TemplateView, CreateView

from product.models import ProductCategory, Product


class CategoryView(ListView):
    model = ProductCategory
    queryset = ProductCategory.objects.all()
    context_object_name = 'category'
    template_name = 'base.html'


class ProductIndexView(ListView):

    def post(self, request):
        search_query = request.POST['search']
        # category_query = request.POST['category']
        category = request.POST.get('category')
        product = Product.objects.all()
        c = ProductCategory.objects.all()
        if category:
            product = product.filter(Q(category_id=category))
        if search_query:
            product= product.filter(Q(title__icontains=search_query))
        return render(request, 'index.html', {'product': product})

    def get(self, request):  # noqa
        product = Product.objects.all()
        return render(request, 'index.html', {'product': product})


class StoreView(TemplateView):
    template_name = 'store.html'


class AddProductView(TemplateView):
    template_name = 'add_product.html'


class BlankView(TemplateView):
    template_name = 'blank.html'


class CheckOutView(TemplateView):
    template_name = 'checkout.html'


class ProductView(CreateView):

    template_name = 'product.html'



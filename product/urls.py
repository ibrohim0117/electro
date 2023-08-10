from django.urls import path

from product.views import ProductIndexView, AddProductView, BlankView, CheckOutView, ProductView, StoreView

urlpatterns = [
    path('', ProductIndexView.as_view(), name='index'),
    path('app-product/', AddProductView.as_view(), name='app_product'),
    path('blank/', BlankView.as_view(), name='blank'),
    path('check-out/', CheckOutView.as_view(), name='check_out'),
    path('product/', ProductView.as_view(), name='product'),
    path('store/', StoreView.as_view(), name='store')
]

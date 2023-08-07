from django.urls import path

from product.views import ProductIndexView

urlpatterns = [
    path('', ProductIndexView.as_view(), name='index'),
]

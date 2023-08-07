from django.urls import path
from apps import views


urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    path('app-product/', views.AddProductView.as_view(), name='app_product'),
    path('blank/', views.BlankView.as_view(), name='blank'),
    path('check-out/', views.CheckOutView.as_view(), name='check_out'),
    path('product/', views.ProductView.as_view(), name='product'),
    path('sign-in/', views.SignInView.as_view(), name='sign_in'),
    path('sign-up/', views.SignUpView.as_view(), name='sign_up'),
    path('store/', views.StoreView.as_view(), name='store')
]

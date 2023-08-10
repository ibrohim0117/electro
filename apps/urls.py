from django.urls import path
from apps import views


urlpatterns = [
    path('sign-in/', views.SignInView.as_view(), name='sign_in'),
    path('sign-up/', views.SignUpView.as_view(), name='sign_up'),
]

from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from apps.forms import RegisterForm, LoginForm
from apps.models import User


class SignInView(LoginView):
    form_class = LoginForm
    template_name = 'sign_in.html'
    next_page = reverse_lazy('index')


class SignUpView(CreateView):
    queryset = User.objects.all()
    form_class = RegisterForm
    template_name = 'sign_up.html'
    success_url = reverse_lazy('sign_in')






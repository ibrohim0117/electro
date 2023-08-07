from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField
from apps.models import User


class RegisterForm(ModelForm):
    confirm_password = CharField(max_length=50)

    class Meta:
        model = User
        fields = ['fullname', 'image', 'email', 'phone', 'address', 'username', 'password', 'confirm_password']

    def clean_password(self):
        if self.cleaned_data['password'] != self.data['confirm_password']:
            raise ValidationError('Password is not valid')
        return make_password(self.cleaned_data['password'])


class LoginForm(AuthenticationForm):
    pass
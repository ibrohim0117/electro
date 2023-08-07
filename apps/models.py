from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ImageField


class User(AbstractUser):
    fullname = CharField(max_length=75)
    image = ImageField(upload_to='user/', blank=True, null=True)
    phone = CharField(max_length=50)
    address = CharField(max_length=255)

    def __str__(self):
        return self.username


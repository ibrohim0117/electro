from django.db import models


class ProductCategory(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug company')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug product')
    category = models.ForeignKey('ProductCategory', models.CASCADE)
    price = models.FloatField(default=0)
    type_choose_size = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
        ('Extra large', 'Extra large')
    )

    type_choose_color = (
        ('Blue', 'Blue'),
        ('White', 'White'),
        ('Red', 'Red'),
        ('Black', 'Black'),
        ('Pink', 'Pink'),
        ('Purple', 'Purple')
    )
    color = models.CharField(choices=type_choose_color, null=True, max_length=255)
    size = models.CharField(choices=type_choose_size, null=True, max_length=255)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    id = models.IntegerField(primary_key=True)
    product_id = models.ForeignKey('Product', models.CASCADE, 'product_image')
    is_general = models.BooleanField(default=False)
    image = models.ImageField(upload_to='product/')


class Card_to(models.Model):
    type_choose_size = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
        ('Extra large', 'Extra large')
    )

    type_choose_color = (
        ('Blue', 'Blue'),
        ('White', 'White'),
        ('Red', 'Red'),
        ('Black', 'Black'),
        ('Pink', 'Pink'),
        ('Purple', 'Purple')
    )
    color = models.CharField(choices=type_choose_color, null=True, max_length=255)
    size = models.CharField(choices=type_choose_size, null=True, max_length=255)
    quantity = models.IntegerField()



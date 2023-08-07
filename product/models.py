from django.db import models


class ProductCategory(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug company')


class Product(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug product')
    category = models.ForeignKey('ProductCategory', models.CASCADE)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    id = models.IntegerField(primary_key=True)
    product_id = models.ForeignKey('Product', models.CASCADE, 'product_image')
    is_general = models.BooleanField(default=False)
    image = models.ImageField(upload_to='product/')


class Detailed(models.Model):
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

    product_id = models.ForeignKey('Product', models.CASCADE, 'product_detailed')
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    detail = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(choices=type_choose_color, null=True, max_length=255)
    size = models.CharField(choices=type_choose_size, null=True, max_length=255)

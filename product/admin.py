from django.contrib import admin
from django.contrib.admin import TabularInline
# Register your models here.
from product.models import Product, ProductCategory, ProductImage


class ProductImageInline(TabularInline):
    model = ProductImage
    fields = 'image',
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'title',
    inlines = [ProductImageInline]


admin.site.register(ProductCategory)
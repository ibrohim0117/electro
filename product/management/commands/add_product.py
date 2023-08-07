from django.core.management.base import BaseCommand
from product.models import ProductCategory, Product, ProductImage
from django.utils.text import slugify
from faker import Faker
from time import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()
        start_time = time()
        for i in range(0, 5):
            title = fake.text(8)
            dis = fake.text(100)
            #add_productcategory
            ProductCategory.objects.create(
                title=title,
                slug=slugify(title)
            )

            # add_product
            p = Product.objects.create(
                title=title,
                slug=slugify(title),
                description=dis,
                category=ProductCategory.objects.all().order_by('?').first(),

            )
            #add_product_image
            ProductImage.objects.create(
                product_id=p,
                image=fake.image_url(),
                is_general=False
            )

            print(f'post {i} has been created')
        end_time = time()
        print('Finished!!!')
        milliseconds = end_time - start_time
        print(f'Time elapsed: {milliseconds} milliseconds')
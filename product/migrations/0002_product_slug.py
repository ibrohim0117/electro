# Generated by Django 4.2.4 on 2023-08-07 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=1, max_length=255, unique=True, verbose_name='Slug product'),
            preserve_default=False,
        ),
    ]

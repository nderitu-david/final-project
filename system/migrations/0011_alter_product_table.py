# Generated by Django 5.0.2 on 2024-02-21 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0010_rename_product_information_product_product_information_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='product',
            table='system_Product',
        ),
    ]

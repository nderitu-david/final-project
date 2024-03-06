# Generated by Django 5.0.2 on 2024-02-21 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0009_section_product_additional_information_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Product_Information',
            new_name='Product_information',
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=500, null=True),
        ),
    ]
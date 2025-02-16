# Generated by Django 5.0.1 on 2024-02-06 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_image', models.ImageField(upload_to='images')),
                ('category_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]

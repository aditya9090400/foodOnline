# Generated by Django 4.2.4 on 2024-01-29 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_vendor_vendor_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='vendor_slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]

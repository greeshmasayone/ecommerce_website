# Generated by Django 4.1.7 on 2023-04-10 07:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_productfabric_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='stock',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Total Stock'),
        ),
    ]

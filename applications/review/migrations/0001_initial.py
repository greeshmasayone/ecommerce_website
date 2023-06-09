# Generated by Django 4.1.7 on 2023-03-26 17:55

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('review', models.TextField(blank=True, null=True, verbose_name='Reviews')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_product_reviews', to='product.product', verbose_name='Product Review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_user_reviews', to=settings.AUTH_USER_MODEL, verbose_name='User Reviews')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('rating', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Rating')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_product_rating', to='product.product', verbose_name='Product Rating')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_user_rating', to=settings.AUTH_USER_MODEL, verbose_name='User Rating')),
            ],
            options={
                'verbose_name': 'Rating',
                'verbose_name_plural': 'wishlist',
            },
        ),
    ]

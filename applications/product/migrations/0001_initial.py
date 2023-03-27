# Generated by Django 4.1.7 on 2023-03-26 17:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'brand',
                'verbose_name_plural': 'brands',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'colour',
                'verbose_name_plural': 'colours',
            },
        ),
        migrations.CreateModel(
            name='Fabric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'fabric',
                'verbose_name_plural': 'fabrics',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='Created at')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_groups', to='product.category', verbose_name='SubCategory')),
            ],
            options={
                'verbose_name': 'group',
                'verbose_name_plural': 'groups',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('price', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Price')),
                ('product_code', models.CharField(max_length=10, unique=True, verbose_name='Product Code')),
                ('cod', models.BooleanField(default=True, verbose_name='Cash on delivery')),
                ('exchange', models.BooleanField(default=True, verbose_name='Exchange')),
                ('product_return', models.BooleanField(default=False, verbose_name='Return')),
                ('return_validity', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(90)], verbose_name='No. of days for return')),
                ('pattern', models.CharField(choices=[('solid', 'Solid'), ('checked', 'Checked'), ('printed', 'Printed'), ('colour_blocked', 'ColourBlocked'), ('faded', 'Faded'), ('self_design', 'SelfDesign'), ('striped', 'Striped'), ('embroidered', 'Embroidered')], max_length=20, verbose_name='Pattern')),
                ('transparency', models.CharField(choices=[('sheer', 'Sheer'), ('opaque', 'Opaque'), ('semi_sheer', 'Semi Sheer')], max_length=20, verbose_name='Transparency')),
                ('sleeve_length', models.CharField(choices=[('long_sleeves', 'Long Sleeves'), ('short_sleeves', 'Short Sleeves'), ('three_quarter_sleeves', 'Three Quarter Sleeves'), ('sleeveless', 'Sleeveless')], max_length=25, verbose_name='Sleeve Length')),
                ('occasion', models.CharField(choices=[('casual', 'Casual'), ('formal', 'Formal'), ('semi_formal', 'Semi Formal'), ('party', 'Party'), ('ethnic', 'Ethnic')], max_length=20, verbose_name='Occasion')),
                ('wash_care', models.CharField(choices=[('machine_wash', 'Machine Wash'), ('dry_clean', 'Dry Clean'), ('hand_wash', 'Hand wash')], max_length=20, verbose_name='Wash Care')),
                ('fit', models.CharField(blank=True, choices=[('regular_fit', 'Regular Fit'), ('slim_fit', 'Slim Fit'), ('skinny_fit', 'Skinny Fit'), ('tailored_fit', 'Tailored Fit')], max_length=20, null=True, verbose_name='Fit')),
                ('collar', models.CharField(blank=True, choices=[('spread_collar', 'Spread Collar'), ('mandarin_collar', 'Mandarin Collar'), ('cutaway_collar', 'Cutaway Collar'), ('band_collar', 'Band Collar'), ('button_down_collar', 'Button Down Collar'), ('collarless', 'Collarless'), ('cuban_collar', 'Cuban Collar'), ('slim_collar', 'Slim Collar')], max_length=20, null=True, verbose_name='Collar')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_product_brand', to='product.brand', verbose_name='Product Brand')),
                ('colour', models.ManyToManyField(related_name='product_colour', to='product.colour', verbose_name='Colour')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_groups', to='product.group', verbose_name='Group')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='Created at')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_categories', to='product.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'subcategory',
                'verbose_name_plural': 'Subcategories',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('stock', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Name')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_stock', to='product.product', verbose_name='Product Stock')),
            ],
            options={
                'verbose_name': 'stock',
                'verbose_name_plural': 'stock',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('chest', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Chest')),
                ('front_length', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Front Length')),
                ('across_shoulder', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Across Shoulder')),
                ('to_fit_waist', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='To Fit Waist')),
                ('inseam_length', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Inseam Length')),
                ('hips', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Hips')),
                ('to_fit_foot_length', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='To fit foot length')),
                ('euro_size', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Euro Size')),
                ('uk_foot_size', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='UK foot size')),
                ('us_foot_size', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='US foot size')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_sizes', to='product.product', verbose_name='Product Size')),
            ],
            options={
                'verbose_name': 'Size',
                'verbose_name_plural': 'Sizes',
            },
        ),
        migrations.CreateModel(
            name='ProductFabric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('fabric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_fabric_details', to='product.fabric', verbose_name='Product Fabric Percentage')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_product_fabric', to='product.product', verbose_name='Product Fabric')),
            ],
            options={
                'verbose_name': 'product_fabric',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images/', verbose_name='Product Image')),
                ('colour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_images_colour', to='product.colour', verbose_name='Product Images colour')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_images', to='product.product', verbose_name='Product Images')),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
            },
        ),
    ]

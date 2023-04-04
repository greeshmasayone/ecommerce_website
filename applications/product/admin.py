from django.contrib import admin
from .models import Category, SubCategory, Group, Colour, Brand, Product, Fabric, Size, Stock, ProductFabric, Image


@admin.register(Category)
class CatAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "created_at"]


@admin.register(SubCategory)
class SubCatAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "category", "pk"]


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "subcategory", "pk"]


@admin.register(Colour)
class ColourCatAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(Fabric)
class FabricAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description", "group", "price", "product_code", "cod", "exchange", "product_return",
                    "return_validity", "brand", "pattern", "transparency", "sleeve_length", "occasion",
                    "wash_care", "fit", "collar"]
    fields = ["name", "description", "group", "price", "product_code", "cod", "exchange", "product_return", "colour",
              "return_validity", "brand", "pattern", "transparency", "sleeve_length", "occasion", "wash_care", "fit",
              "collar"]
    search_fields = ["id", "group", "name", "cod", "product_return", "colour", "brand", "pattern", "sleeve_length",
                     "occasion", "fit", "collar"]
    list_display_links = ["name"]


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'product', 'chest', 'front_length', 'across_shoulder', 'to_fit_waist', 'inseam_length',
                    'hips', 'to_fit_foot_length', 'euro_size', 'uk_foot_size', 'us_foot_size']
    fields = ['name', 'product', 'chest', 'front_length', 'across_shoulder', 'to_fit_waist', 'inseam_length', 'hips',
              'to_fit_foot_length', 'euro_size', 'uk_foot_size', 'us_foot_size']
    search_fields = ['name', 'product', 'chest', 'front_length', 'across_shoulder', 'to_fit_waist', 'inseam_length',
                     'hips', 'to_fit_foot_length', 'euro_size', 'uk_foot_size', 'us_foot_size']
    list_filter = ['name', 'product', 'chest', 'front_length', 'across_shoulder', 'to_fit_waist', 'inseam_length',
                   'hips', 'to_fit_foot_length', 'euro_size', 'uk_foot_size', 'us_foot_size']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'product', 'colour']
    fields = ['image', 'product', 'colour']
    search_fields = ['product', 'colour']
    list_filter = ['product', 'colour']


@admin.register(ProductFabric)
class ProductFabricAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'fabric', 'percentage']
    fields = ['product', 'fabric', 'percentage']
    search_fields = ['product', 'fabric']
    list_filter = ['product', 'fabric']


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'stock']
    fields = ['product', 'stock']
    search_fields = ['product']
    list_filter = ['product']

from rest_framework import serializers
from .models import Product, Category, SubCategory, Group


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "title", "description"]


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ["id", "title", "description", "category"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "title", "description", "subcategory"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "group", "description", "price", "product_code", "cod", "exchange", "product_return",
                  "colour", "return_validity", "brand", "pattern", "transparency", "sleeve_length", "occasion",
                  "wash_care", "fit", "collar"]

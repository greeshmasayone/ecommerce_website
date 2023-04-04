from rest_framework import serializers
from .models import Wishlist, Cart, Address, Order
from django.db.models import F, Sum


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ["id", "user", "product"]


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["id", "user", "product", "product_quantity", "product_cost"]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["id", "user", "locality", "city", "state", "zipcode", "type", "is_default"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "user", "address", "amount", "coupon", "phone_number", "order_id", "ordered_date",
                  "order_status", "is_return", "return_reason", "is_exchange"]

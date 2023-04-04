from django.contrib import admin
from .models import Cart, Wishlist, Order, Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "locality", "city", "state", "zipcode", "type", "is_default"]
    fields = ["user", "locality", "city", "state", "zipcode", "type", "is_default"]
    search_fields = ["city", "state",  "zipcode"]
    list_display_links = ["user"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "address", "amount", "coupon", "phone_number", "order_id", "ordered_date",
                    "order_status", "is_return", "return_reason", "is_exchange"]
    fields = ["product", "user", "address", "amount", "coupon", "phone_number", "order_id", "ordered_date",
              "order_status", "is_return", "return_reason", "is_exchange"]
    search_fields = ["product", "user", "order_id"]
    list_display_links = ["user"]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "product", "product_quantity"]
    fields = ["user", "product", "product_quantity"]
    search_fields = ["user", "product"]
    list_display_links = ["user"]


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "product"]
    fields = ["user", "product"]
    search_fields = ["user", "product"]
    list_display_links = ["user"]

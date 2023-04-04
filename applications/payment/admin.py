from django.contrib import admin
from .models import Coupon, Payment, Refund


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "code", "expiry_date", "is_active", "usage_limit", "usage_type", "coupon_type",
                    "value"]
    fields = ["name", "code", "expiry_date", "is_active", "usage_limit", "usage_type", "coupon_type", "value"]
    search_fields = ["name", "code", "is_active", "usage_type", "coupon_type"]
    list_display_links = ["name"]


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ["id", "amount", "date", "user", "coupon", "mode"]
    fields = ["amount", "date", "user", "coupon", "mode"]
    list_display_links = ["id"]


@admin.register(Refund)
class RefundAdmin(admin.ModelAdmin):
    list_display = ["id", "amount", "refund_requested", "refund_granted"]
    fields = ["amount", "refund_requested", "refund_granted"]
    list_display_links = ["id"]

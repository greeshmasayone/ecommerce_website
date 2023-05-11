from rest_framework import serializers
from .models import Coupon, Payment, Refund


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ["id", "name", "code", "expiry_date", "is_active", "usage_limit", "usage_type", "coupon_type", "value"]


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ["id", "amount", "date", "user", "coupon", "mode"]


class RefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refund
        fields = ["id", "amount", "refund_requested", "refund_granted"]

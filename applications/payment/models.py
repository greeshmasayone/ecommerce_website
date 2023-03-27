from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from ..common.models import DateBaseModel
from ..customer.models import User


class Coupon(DateBaseModel):
    SINGLE_USE = 'single_use'
    MULTI_USE = 'multi_use'

    USAGE_TYPE = (
        (SINGLE_USE, "Single Use"),
        (MULTI_USE, "Multi Use")
    )

    PRICE = 'price'
    PERCENTAGE = 'percentage'

    COUPON_TYPE = (
        (PRICE, "Price"),
        (PERCENTAGE, "Percentage")
    )
    name = models.CharField(_("Name"), max_length=100)
    code = models.CharField(_("Coupon Code"), unique=True, max_length=10)
    expiry_date = models.DateField(_("Expiry Date"))
    is_active = models.BooleanField(_("Is Active"), default=True)
    usage_limit = models.PositiveIntegerField(_("Coupon Usage Limit"), validators=[MinValueValidator(0)], null=True, blank=True)
    usage_type = models.CharField(_("Number of usage"), max_length=40, choices=USAGE_TYPE)
    coupon_type = models.CharField(_("Coupon Type"), max_length=40, choices=COUPON_TYPE)
    value = models.CharField(_("Value"), max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "Coupon"
        verbose_name_plural = "Coupons"

    def __str__(self):
        return self.name


class Payment(DateBaseModel):
    UPI = 'upi'
    CREDIT_CARD = 'credit_card'
    PAYTM = 'paytm'
    NET_BANKING = 'net_banking'
    EMI = 'emi'
    CASH_ON_DELIVERY = 'cash_on_delivery'

    PAYMENT_MODE = (
        (UPI, "UPI"),
        (CREDIT_CARD, "Credit Card"),
        (PAYTM, "Paytm"),
        (NET_BANKING, "Net Banking"),
        (EMI, "Emi"),
        (CASH_ON_DELIVERY, 'Cash on delivery')
    )
    amount = models.DecimalField(_("Amount Payed"), decimal_places=2, max_digits=10)
    date = models.DateField(_("Payment Date"), null=True, blank=True, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Payment"), related_name='get_payment')
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE, verbose_name=_("Coupons"), related_name='get_coupons')
    mode = models.CharField(_("Mode Of Payment"), max_length=40, choices=PAYMENT_MODE)

    class Meta:
        verbose_name = "payment"
        verbose_name_plural = "payments"

    def __str__(self):
        return self.amount


class Refund(DateBaseModel):
    amount = models.ForeignKey(Payment, on_delete=models.CASCADE, verbose_name=_("Refund"), related_name='get_refund')
    refund_requested = models.BooleanField(_("Is Refund Requested"), default=False)
    refund_granted = models.BooleanField(_("Is refund accepted"), default=False)

    class Meta:
        verbose_name = "refund"
        verbose_name_plural = "refunds"


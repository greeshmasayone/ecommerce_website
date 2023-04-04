from django.db import models
from django.utils.translation import gettext_lazy as _
from ..common.models import DateBaseModel
from django.core.validators import MinValueValidator
from ..customer.models import User
from ..payment.models import Coupon
from ..product.models import Product


class Address(DateBaseModel):
    HOME = 'home'
    OFFICE = 'office'
    OTHER = 'other'

    ADDRESS_TYPE = (
        (HOME, "Home"),
        (OFFICE, "Office"),
        (OTHER, "Other")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User Address"), related_name='get_address')
    locality = models.TextField(_("Locality"))
    city = models.CharField(_("City"), max_length=200)
    state = models.TextField(_("City"))
    zipcode = models.IntegerField(_("zip code"))
    type = models.CharField(_("Address Type"), max_length=50, choices=ADDRESS_TYPE, null=True, blank=True)
    is_default = models.BooleanField(_("Is Default Address"), default=True)

    class Meta:
        verbose_name = "Address"


class Order(DateBaseModel):
    PROCESSING = 'processing'
    SHIPPED = 'shipped'
    IN_TRANSITION = 'in_transition'
    DELIVERED = 'delivered'

    ORDER_STATUS = (
        (PROCESSING, "Processing"),
        (SHIPPED, "Shipped"),
        (IN_TRANSITION, "In Transition"),
        (DELIVERED, "Delivered")
    )

    BOUGHT_BY_MISTAKE = 'bought_by_mistake'
    BETTER_PRICE_AVAILABLE = 'better_price_available'
    INADEQUATE_QUALITY = 'inadequate_quality'
    NOT_USEFUL = 'not_useful'
    PRODUCT_DAMAGED = 'product_damaged'
    LATE_ARRIVAL = 'late_arrival'
    MISSING_ACCESSORIES = 'missing_accessories'
    WRONG_ITEM_SENT = 'wrong_item_sent'
    SHIPPING_BOX_DAMAGED = 'shipping_box_damaged'
    INADEQUATE_DESCRIPTION = 'inadequate_description'

    RETURN_REASON = (
        (BOUGHT_BY_MISTAKE, "Bought By Mistake"),
        (BETTER_PRICE_AVAILABLE, "Better Price Available"),
        (INADEQUATE_QUALITY, "Inadequate Quality"),
        (NOT_USEFUL, "Not Useful"),
        (PRODUCT_DAMAGED, "Product Damaged"),
        (LATE_ARRIVAL, "Late Arrival"),
        (MISSING_ACCESSORIES, "Missing Accesories"),
        (WRONG_ITEM_SENT, "Wrong Item Sent"),
        (SHIPPING_BOX_DAMAGED, "Shipping box Damaged"),
        (INADEQUATE_DESCRIPTION, "Inadequate Description")
    )
    product = models.ManyToManyField(Product, verbose_name=_("Product"), related_name='product_order')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User Orders"), related_name='get_orders')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, verbose_name=_("User Address"), related_name='get_address')
    amount = models.DecimalField(_("Order Amount"), max_digits=12, decimal_places=2, default=1.00, validators=[MinValueValidator(1.00)])
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE, verbose_name=_("User Coupon"), related_name='get_coupon')
    phone_number = models.CharField(_("Mobile Number"), max_length=15, null=False)
    order_id = models.CharField(_("Order Id"), max_length=10, null=False, unique=True)
    ordered_date = models.DateField(_("Order Date"))
    order_status = models.CharField(_("Order Status"), max_length=40, choices=ORDER_STATUS)
    is_return = models.BooleanField(_("Is Return"), default=False)
    return_reason = models.CharField(_("Return Reason"), max_length=200, choices=RETURN_REASON)
    is_exchange = models.BooleanField(_("Is Exchange"), default=False)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class Wishlist(DateBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Wishlist"), related_name='get_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("User Products"), related_name='get_wishlist')

    class Meta:
        verbose_name = "wishlist"
        verbose_name_plural = "wishlist"


class Cart(DateBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Cart"), related_name='get_cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("User Items"), related_name='get_cart')
    product_quantity = models.IntegerField(_("Product quantity"), default=1)

    class Meta:
        verbose_name = "cart"
        verbose_name_plural = "cart"




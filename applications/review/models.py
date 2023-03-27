from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from ..customer.models import User
from ..common.models import DateBaseModel
from ..product.models import Product


class Rating(DateBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User Rating"), related_name='get_user_rating')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product Rating"), related_name='get_product_rating')
    rating = models.PositiveSmallIntegerField(_('Rating'), validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True)

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "wishlist"


class Review(DateBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User Reviews"),
                             related_name='get_user_reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product Review"), related_name='get_product_reviews')
    review = models.TextField(_("Reviews"), null=True, blank=True)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

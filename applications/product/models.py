from django.db import models
from django.utils.translation import gettext_lazy as _
from ..common.models import DateBaseModel
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(DateBaseModel):
    title = models.CharField(_("Name"), max_length=200)
    description = models.TextField(_("Description"), null=True, blank=True)
    created_at = models.DateTimeField(_("Created at"), null=True, blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class SubCategory(DateBaseModel):
    title = models.CharField(_("Name"), max_length=200)
    description = models.TextField(_("Description"), null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("Category"),
                                 related_name='get_categories')
    created_at = models.DateTimeField(_("Created at"), null=True, blank=True)

    class Meta:
        verbose_name = "subcategory"
        verbose_name_plural = "Subcategories"

    def __str__(self):
        return self.title


class Group(DateBaseModel):
    title = models.CharField(_("Name"), max_length=200)
    description = models.TextField(_("Description"), null=True, blank=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name=_("SubCategory"), related_name='get_groups')
    created_at = models.DateTimeField(_("Created at"), null=True, blank=True)

    class Meta:
        verbose_name = "group"
        verbose_name_plural = "groups"

    def __str__(self):
        return self.title


class Colour(DateBaseModel):
    name = models.CharField(_("Name"), max_length=200)

    class Meta:
        verbose_name = "colour"
        verbose_name_plural = "colours"

    def __str__(self):
        return self.name


class Brand(DateBaseModel):
    name = models.CharField(_("Name"), max_length=200)

    class Meta:
        verbose_name = "brand"
        verbose_name_plural = "brands"

    def __str__(self):
        return self.name


class Product(DateBaseModel):
    SOLID = 'solid'
    CHECKED = 'checked'
    PRINTED = 'printed'
    COLOUR_BLOCKED = 'colour_blocked'
    FADED = 'faded'
    SELF_DESIGN = 'self_design'
    STRIPED = 'striped'
    EMBROIDERED = 'embroidered'

    PATTERN_CHOICES = (
        (SOLID, "Solid"),
        (CHECKED, "Checked"),
        (PRINTED, "Printed"),
        (COLOUR_BLOCKED, "ColourBlocked"),
        (FADED, "Faded"),
        (SELF_DESIGN, "SelfDesign"),
        (STRIPED, "Striped"),
        (EMBROIDERED, "Embroidered")
    )

    SHEER = 'sheer'
    OPAQUE = 'opaque'
    SEMI_SHEER = 'semi_sheer'

    TRANSPARENCY_CHOICES = (
        (SHEER, "Sheer"),
        (OPAQUE, "Opaque"),
        (SEMI_SHEER, "Semi Sheer")
    )

    LONG_SLEEVES = 'long_sleeves'
    SHORT_SLEEVES = 'short_sleeves'
    THREE_QUARTER_SLEEVES = 'three_quarter_sleeves'
    SLEEVELESS = 'sleeveless'
    NOT_APPLICABLE = 'not_applicable'

    SLEEVE_LENGTH_CHOICES = (
        (LONG_SLEEVES, "Long Sleeves"),
        (SHORT_SLEEVES, "Short Sleeves"),
        (THREE_QUARTER_SLEEVES, "Three Quarter Sleeves"),
        (SLEEVELESS, "Sleeveless"),
        (NOT_APPLICABLE, "Not Applicable")
    )

    CASUAL = 'casual'
    FORMAL = 'formal'
    SEMI_FORMAL = 'semi_formal'
    PARTY = 'party'
    ETHNIC = 'ethnic'

    OCCASION_CHOICES = (
        (CASUAL, "Casual"),
        (FORMAL, "Formal"),
        (SEMI_FORMAL, "Semi Formal"),
        (PARTY, "Party"),
        (ETHNIC, "Ethnic")
    )

    MACHINE_WASH = 'machine_wash'
    DRY_CLEAN = 'dry_clean'
    HAND_WASH = 'hand_wash'

    WASH_CARE_CHOICES = (
        (MACHINE_WASH, "Machine Wash"),
        (DRY_CLEAN, "Dry Clean"),
        (HAND_WASH, "Hand wash")
    )

    REGULAR_FIT = 'regular_fit'
    SLIM_FIT = 'slim_fit'
    SKINNY_FIT = 'skinny_fit'
    TAILORED_FIT = 'tailored_fit'

    FIT_CHOICES = (
        (REGULAR_FIT, "Regular Fit"),
        (SLIM_FIT, "Slim Fit"),
        (SKINNY_FIT, "Skinny Fit"),
        (TAILORED_FIT, "Tailored Fit")
    )

    SPREAD_COLLAR = 'spread_collar'
    MANDARIN_COLLAR = 'mandarin_collar'
    CUTAWAY_COLLAR = 'cutaway_collar'
    BAND_COLLAR = 'band_collar'
    BUTTON_DOWN_COLLAR = 'button_down_collar'
    COLLARLESS = 'collarless'
    CUBON_COLLAR = 'cuban_collar'
    SLIM_COLLAR = 'slim_collar'

    COLLAR_CHOICES = (
        (SPREAD_COLLAR, "Spread Collar"),
        (MANDARIN_COLLAR, "Mandarin Collar"),
        (CUTAWAY_COLLAR, "Cutaway Collar"),
        (BAND_COLLAR, "Band Collar"),
        (BUTTON_DOWN_COLLAR, "Button Down Collar"),
        (COLLARLESS, "Collarless"),
        (CUBON_COLLAR, "Cuban Collar"),
        (SLIM_COLLAR, "Slim Collar")
    )

    name = models.CharField(_("Name"), max_length=200)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name=_("Group"), related_name='product_groups')
    description = models.TextField(_("Description"), null=True, blank=True)
    price = models.PositiveSmallIntegerField(_("Price"), validators=[MinValueValidator(0)])
    product_code = models.CharField(_("Product Code"), unique=True, max_length=10)
    cod = models.BooleanField(_("Cash on delivery"), default=True)
    exchange = models.BooleanField(_("Exchange"), default=True)
    product_return = models.BooleanField(_("Return"), default=False)
    colour = models.ManyToManyField(Colour, verbose_name=_("Colour"), related_name='product_colour')
    return_validity = models.PositiveSmallIntegerField(_("No. of days for return"), validators=[MinValueValidator(0), MaxValueValidator(90)],
                                                       null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name=_("Product Brand"), related_name='get_product_brand')
    pattern = models.CharField(_("Pattern"), max_length=20, choices=PATTERN_CHOICES)
    transparency = models.CharField(_("Transparency"), max_length=20, choices=TRANSPARENCY_CHOICES)
    sleeve_length = models.CharField(_("Sleeve Length"), max_length=25, choices=SLEEVE_LENGTH_CHOICES)
    occasion = models.CharField(_("Occasion"), max_length=20, choices=OCCASION_CHOICES)
    wash_care = models.CharField(_("Wash Care"), max_length=20, choices=WASH_CARE_CHOICES)
    fit = models.CharField(_("Fit"), max_length=20, choices=FIT_CHOICES, null=True, blank=True)
    collar = models.CharField(_("Collar"), max_length=20, choices=COLLAR_CHOICES, null=True, blank=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name


class Fabric(DateBaseModel):
    name = models.CharField(_("Name"), max_length=200)

    class Meta:
        verbose_name = "fabric"
        verbose_name_plural = "fabrics"

    def __str__(self):
        return self.name


class Size(DateBaseModel):
    name = models.CharField(_("Name"), max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product Size"), related_name='get_sizes')
    chest = models.DecimalField(_("Chest"), decimal_places=1, max_digits=3, null=True, blank=True)
    front_length = models.DecimalField(_("Front Length"), decimal_places=1, max_digits=3, null=True, blank=True)
    across_shoulder = models.DecimalField(_("Across Shoulder"), decimal_places=1, max_digits=3, null=True, blank=True)
    to_fit_waist = models.DecimalField(_("To Fit Waist"), decimal_places=1, max_digits=3, null=True, blank=True)
    inseam_length = models.DecimalField(_("Inseam Length"), decimal_places=1, max_digits=3,  null=True, blank=True)
    hips = models.DecimalField(_("Hips"), decimal_places=1, max_digits=3, null=True, blank=True)
    to_fit_foot_length = models.DecimalField(_("To fit foot length"), decimal_places=1, max_digits=3, null=True, blank=True)
    euro_size = models.DecimalField(_("Euro Size"), decimal_places=1, max_digits=3, null=True, blank=True)
    uk_foot_size = models.DecimalField(_("UK foot size"), decimal_places=1, max_digits=3, null=True, blank=True)
    us_foot_size = models.DecimalField(_("US foot size"), decimal_places=1, max_digits=3, null=True, blank=True)

    class Meta:
        verbose_name = "Size"
        verbose_name_plural = "Sizes"

    def __str__(self):
        return self.name


class Image(DateBaseModel):
    image = models.ImageField(_("Product Image"), null=True, blank=True, upload_to='product_images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product Images"), related_name='get_images')
    colour = models.ForeignKey(Colour, on_delete=models.CASCADE, verbose_name=_("Product Images colour"), related_name='get_images_colour')

    class Meta:
        verbose_name = "image"
        verbose_name_plural = "images"


class ProductFabric(DateBaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product Fabric"), related_name='get_product_fabric')
    fabric = models.ForeignKey(Fabric, on_delete=models.CASCADE, verbose_name=_("Product Fabric Percentage"), related_name='get_fabric_details')
    percentage = models.CharField(_("Percentage"), max_length=200, default='default_value', null=True, blank=True)

    class Meta:
        verbose_name = "product_fabric"


class Stock(DateBaseModel):
    stock = models.PositiveSmallIntegerField(_("Total Stock"), validators=[MinValueValidator(0)])
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product Stock"), related_name='get_stock')

    class Meta:
        verbose_name = "stock"
        verbose_name_plural = "stock"











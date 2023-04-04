from django.contrib import admin
from .models import Rating, Review


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "product", "rating"]
    fields = ["user", "product", "rating"]
    search_fields = ["product"]
    list_display_links = ["id"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "product", "review"]
    fields = ["id", "user", "product", "review"]
    search_fields = ["product"]
    list_display_links = ["id"]

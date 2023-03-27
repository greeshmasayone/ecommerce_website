from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "id", "email", "first_name", "last_name", "username", "phone", "gender", "date_of_birth"
    ]
    fields = [
         "username", "email", "first_name", "last_name", "phone", "gender", "date_of_birth"
    ]
    search_fields = [
        "id", "username", "email", "first_name", "last_name"
    ]
    list_display_links = ["id", "username"]
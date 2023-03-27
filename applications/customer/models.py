from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from ..common.models import DateBaseModel


class User(DateBaseModel, AbstractUser):
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'
    GENDER_CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other")
    )
    email = models.EmailField(_("Email"), unique=True)
    phone = models.CharField(_("Phone number"), max_length=15)
    profile_pic = models.ImageField(_("Image"), upload_to="user-images/", null=True, blank=True)

    gender = models.CharField(_("Gender"), max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    date_of_birth = models.DateField(_("DOB"), null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email

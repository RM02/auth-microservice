from django.db import models
from django.contrib.auth.models import AbstractUser
from authservice.settings import DEFAULT_PASS
from django.contrib.auth.hashers import make_password
from .managers import CustomUserManager

class User(AbstractUser):
    dni = models.CharField(max_length=50, null=True)
    document_type=models.CharField(max_length=50, choices=[("C", "Cedula"), ("P", "Pasaporte"), ("J", "RIF")], null=True)
    password=models.CharField(max_length=250, auto_created=True, default=make_password(DEFAULT_PASS))

    address = models.CharField(max_length=250, null=True)
    position = models.CharField(max_length=250, null=True)

    primary_phone_number= models.CharField(max_length=250, null=True)
    secondary_phone_number= models.CharField(max_length=250, null=True)

    REQUIRED_FIELDS = ('email',)

    objects = CustomUserManager()

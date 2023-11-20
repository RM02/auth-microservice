from django.db import models
from django.contrib.auth.models import AbstractUser
from authservice.settings import DEFAULT_PASS
from uuid import uuid4

from .managers import CustomUserManager

class User(AbstractUser):
    dni = models.CharField(max_length=50, null=True)
    document_type=models.CharField(max_length=250, choices=[("C", "Cedula"), ("P", "Pasaporte"), ("J", "RIF")], null=True)
    #password=models.CharField(max_length=250, auto_created=True, default=make_password(DEFAULT_PASS))

    address = models.CharField(max_length=250, null=True)
    position = models.CharField(max_length=250, null=True)

    primary_phone_number= models.CharField(max_length=250, null=True)
    secondary_phone_number= models.CharField(max_length=250, null=True)

    password = models.CharField(max_length=250, blank=False)
    username = models.CharField(max_length=250, blank=True)

    email = models.CharField(max_length=250, unique=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name']


    objects = CustomUserManager()

class Invitation(models.Model):
    id = models.CharField(default=uuid4(), unique=True, primary_key=True, auto_created=True, max_length=250)
    
    email = models.EmailField(max_length=250)
    code = models.CharField(max_length=255, auto_created=True, default=uuid4())
    
    created_by = models.CharField(max_length=250, blank=True)
    
    sent_at = models.DateTimeField(auto_now_add=True)
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    dni = models.CharField(max_length=50)
    document_type=models.CharField(max_length=50, choices=[("V", "Venezolano"), ("E", "Extranjero")])

    address = models.CharField(max_length=250)
    primary_phone_number= models.CharField(max_length=250)
    secondary_phone_number= models.CharField(max_length=250)



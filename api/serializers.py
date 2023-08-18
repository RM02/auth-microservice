
from django.core.mail import send_mail
from authservice.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string

from .models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        ordering = ['id']
        fields = ['id', 'dni', 'address', 'username', 'first_name', 'last_name', 'email', 'position', 'groups', 'primary_phone_number', 'secondary_phone_number', 'is_staff', 'date_joined']

    # def create(self, data):
    #     instance = super(UserSerializer, self).create(data)
    #     send_mail(
    #         'ESos',
    #         from_email=EMAIL_HOST_USER,
    #         html_message=render_to_string("registration.html"),
    #         message='Su cuenta ha sido creada exitosamente!',
    #         recipient_list=[data.get("email")]
    #     )
    #     return instance

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.first_name
        print(cls)
        # ...

        return token
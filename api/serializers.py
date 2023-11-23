
from django.core.mail import send_mail
from authservice.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string

from .models import User, Invitation
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model

from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        password = make_password(validated_data['password'])
        validated_data['password'] = password
        user = User.objects.create(**validated_data)
        return user
    class Meta:
        model = User
        ordering = ['id']
        fields = ['id', 'dni', 'address', 'username', 'first_name', 'last_name', 'email', 'password', 'position', 'primary_phone_number', 'secondary_phone_number', 'is_staff', 'date_joined']

    # def create(self, data):
    #     instance = super(UserSerializer, self).create(data)

    #     """ send_mail(
    #         'Bteno',
    #         from_email=EMAIL_HOST_USER,
    #         html_message=render_to_string("registration.html", context={ "first_name": data.get("first_name") }),
    #         message='Bienvenido a Bteno!',
    #         recipient_list=[data.get("email")]
    #     ) """
    #     return instance

class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = ('id', 'email', 'code', 'sent_at', 'created_by')

    def create(self, data):

        instance = super(InvitationSerializer, self).create(data)

        send_mail(
            subject='Bteno',
            message='Unete a la comunidad Bteno.com',
            html_message=render_to_string("invitation.html", context={ "email": data.get("email") }),
            from_email=EMAIL_HOST_USER,
            recipient_list=[data.get("email")],
            fail_silently=False,
        )
        return instance

    def put(self, data):
        instance = super(UserSerializer, self).create(data)

        invitation = Invitation.objects.filter(code=data.get("code"))
        invitation.delete()

        return instance

class TokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = get_user_model().USERNAME_FIELD
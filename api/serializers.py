
from .models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        ordering = ['id']
        fields = ['id', 'dni', 'address', 'username', 'first_name', 'last_name', 'email', 'groups', 'is_staff', 'date_joined']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        # ...

        return token
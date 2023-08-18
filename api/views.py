from .models import User
from rest_framework import filters
from rest_framework import viewsets, generics
from rest_framework import permissions
from api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'dni', 'email', 'username']
    
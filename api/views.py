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
    permission_classes = [permissions.AllowAny]
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['username', 'dni']
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = User.objects.all()
        username = self.request.query_params.get('username')
        dni = self.request.query_params.get('dni')
        
        if username is not None:
            queryset = queryset.filter(username=username)
        elif dni is not None:
            queryset = queryset.filter(dni=dni)

        return queryset
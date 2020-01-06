from rest_framework import viewsets

from api.user.serializers import UserSerializer, RoleSerializer
from user.models import User, Role

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets

from user.serializers import CreateUserSerializer, ListUsersSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = ListUsersSerializer

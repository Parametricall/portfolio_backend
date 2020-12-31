from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView, ListAPIView, \
    RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.settings import api_settings
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from user.serializers import UsersSerializer, AuthTokenSerializer


class CreateView(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UsersSerializer


class ListView(ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.IsAdminUser]


class RetrieveView(RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.IsAuthenticated]


class UpdateView(UpdateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.IsAuthenticated]


class DestroyView(DestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })

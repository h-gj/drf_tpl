# Create your views here.
from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from users.serializers import UserSerializer


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = ()


from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import UserSerializer, ChangePasswordSerializer, UpdateUserSerializer
from .models import UserProfile


class UserCreate(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )


class ChangePasswordView(generics.UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)


class UpdateProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UpdateUserSerializer

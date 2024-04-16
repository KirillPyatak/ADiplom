from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from accounts.models import User
from accounts.api.serializer.serializer import UserProfileSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer


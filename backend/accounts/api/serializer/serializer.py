# accounts/api/serializers.py

from rest_framework import serializers
from accounts.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #exclude = ("password", "last_login", "is_active", "is_staff")
        fields = '__all__'
# accounts/api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.api.views.views import UserProfileViewSet

router = DefaultRouter()

router.register('User', UserProfileViewSet, basename='User')

urlpatterns = [
    path('', include(router.urls)),]

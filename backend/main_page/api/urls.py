# main_page/api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main_page.api.views.views import *
#from accounts.api.views.views import *

app_name = 'main_page'

router = DefaultRouter()
router.register(r'PublicationViewSet', PublicationViewSet, basename='PublicationViewSet')
router.register(r'PublicationTypeViewSet', PublicationTypeViewSet, basename='PublicationTypeViewSet')
router.register(r'Journal', JournalViewSet, basename='Journal')
router.register(r'AuthorViewSet', AuthorViewSet, basename='AuthorViewSet')

urlpatterns = [
    path('', include(router.urls)),
    #path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail')
]
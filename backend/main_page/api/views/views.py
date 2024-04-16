# main_page/api/views/views.py
import django_filters
from rest_framework import viewsets, filters
from main_page.models import *
from main_page.api.serializers.serializer import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from main_page.api.filters import PublicationFilter


class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = PublicationFilter
    search_fields = ['title', 'authors__name', 'journal__name']
    ordering_fields = ['created_at', 'citation_count']


class PublicationTypeViewSet(viewsets.ModelViewSet):
    queryset = PublicationType.objects.all()
    serializer_class = PublicationTypeSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Authorship.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['user__name', 'job_title', 'workplace', 'education']
    ordering_fields = ['user__name', 'created_at']
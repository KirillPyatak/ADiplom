import django_filters
from main_page.models import Publication

class PublicationFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    authors = django_filters.CharFilter(field_name='authors__name', lookup_expr='icontains')
    journal = django_filters.CharFilter(field_name='journal__name', lookup_expr='icontains')
    types = django_filters.CharFilter(field_name='types__name', lookup_expr='icontains')
    class Meta:
        model = Publication
        fields = ['title', 'authors', 'journal', 'types']
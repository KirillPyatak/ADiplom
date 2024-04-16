# main_page/api/serializers/serializer.py

from rest_framework import serializers
from main_page.models import Publication,PublicationType,Authorship,Journal


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authorship
        fields = '__all__'

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        exclude = ['id']
class PublicationSerializer(serializers.ModelSerializer):
    journal = JournalSerializer(read_only=True)
    types = JournalSerializer(read_only=True, many=True)
    authors = serializers.SerializerMethodField('get_authors')  # Use SerializerMethodField to customize authors field


    def get_authors(self, obj):
        authors = obj.authors.all()  # Retrieve all authors related to the publication
        author_names = [author.name for author in authors]  # Extract names from User objects
        return author_names
    class Meta:
        model = Publication
        fields = '__all__'

class PublicationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicationType
        fields = '__all__'
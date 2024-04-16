# main_page/models.py
from django.utils.translation import gettext_lazy as _
from django.db import models
from accounts.models import User
class PublicationType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Journal(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Publication(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Changed data type to DateTimeField
    is_verified = models.BooleanField(default=False)
    citation_count = models.PositiveIntegerField(default=0)
    journal = models.ForeignKey(Journal, on_delete=models.SET_NULL, null=True, related_name='publications')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    types = models.ManyToManyField(PublicationType, related_name='publications')
    authors = models.ManyToManyField(User, through='Authorship', related_name='authored_publications')

    def increase_citation_count(self):
        self.citation_count += 1
        self.save()

    def __str__(self):
        return f"{self.title} ({self.authors.count()} authors)"

class Authorship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} is an author of {self.publication.title}"

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribers', null=True, blank=True)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE, related_name='subscribers', null=True, blank=True)

    def __str__(self):
        return f"{self.user} follows {self.author}"
# main_page/models.py

from django.db import models
from accounts.models import User


class ScientificActivity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='scientific_activity')
    publication_count = models.PositiveIntegerField(default=0)
    conference_participation = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.name}'s Scientific Activity"


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.name}"


class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='schedules')
    date = models.DateField()
    events = models.TextField()

    def __str__(self):
        return f"Schedule for {self.user.name} on {self.date}"


class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat message from {self.sender.name} to {self.receiver.name}"

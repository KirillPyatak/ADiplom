# main_page/serializers.py

from rest_framework import serializers
from main_page.models import *

class ScientificActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ScientificActivity
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'

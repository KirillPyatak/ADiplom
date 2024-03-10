# main_page/api/views.py

from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from main_page.models import *
from main_page.api.serializers import (
    ScientificActivitySerializer,
    NotificationSerializer,
    ScheduleSerializer,
    ChatMessageSerializer
)


class ScientificActivityViewSet(viewsets.ModelViewSet):
    queryset = ScientificActivity.objects.all()
    serializer_class = ScientificActivitySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ChatMessageViewSet(viewsets.ModelViewSet):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class NotificationMarkAsReadAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, notification_id):
        notification = Notification.objects.get(id=notification_id)
        if notification.user == request.user:
            notification.delete()
            return Response({"message": "Notification marked as read"}, status=200)
        return Response({"error": "You do not have permission to perform this action"}, status=403)


class ScheduleRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Schedule.objects.filter(user=self.request.user)


class ScientificActivityRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = ScientificActivity.objects.all()
    serializer_class = ScientificActivitySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ScientificActivity.objects.filter(user=self.request.user)

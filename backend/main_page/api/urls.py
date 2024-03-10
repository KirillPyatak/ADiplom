# main_page/api/urls.py

from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    ScientificActivityViewSet,
    NotificationViewSet,
    ScheduleViewSet,
    ChatMessageViewSet,
    NotificationMarkAsReadAPIView,
    ScheduleRetrieveUpdateAPIView,
    ScientificActivityRetrieveUpdateAPIView,
)

router = DefaultRouter()
router.register(r'scientific-activity', ScientificActivityViewSet, basename='scientific-activity')
router.register(r'notifications', NotificationViewSet, basename='notifications')
router.register(r'schedules', ScheduleViewSet, basename='schedules')
router.register(r'chat-messages', ChatMessageViewSet, basename='chat-messages')

urlpatterns = router.urls + [
    path('notifications/mark-as-read/<int:notification_id>/', NotificationMarkAsReadAPIView.as_view(), name='notification-mark-as-read'),
    path('schedules/<int:pk>/', ScheduleRetrieveUpdateAPIView.as_view(), name='schedule-retrieve-update'),
    path('scientific-activity/<int:pk>/', ScientificActivityRetrieveUpdateAPIView.as_view(), name='scientific-activity-retrieve-update'),
]

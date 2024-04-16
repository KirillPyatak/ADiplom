# main_page/admin.py

from django.contrib import admin
from .models import Publication, PublicationType, Authorship,Journal

admin.site.register(Publication)
admin.site.register(Journal)

admin.site.register(PublicationType)

admin.site.register(Authorship)
# admin.site.register(Notification)
# admin.site.register(Schedule)
# admin.site.register(ChatMessage)

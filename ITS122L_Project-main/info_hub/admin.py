from django.contrib import admin

from .models import Post, Event, Profile, Announcement

# Register your models here.
admin.site.register(Post)
admin.site.register(Event)
admin.site.register(Announcement)
admin.site.register(Profile)

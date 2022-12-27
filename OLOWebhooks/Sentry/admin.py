from django.contrib import admin
from Sentry.models import WebHook, Location

# Register your models here.

admin.site.register(WebHook)
admin.site.register(Location)
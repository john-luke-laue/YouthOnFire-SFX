from django.contrib import admin

from main.models import Event
from main.models import Email

admin.site.register(Event)
admin.site.register(Email)
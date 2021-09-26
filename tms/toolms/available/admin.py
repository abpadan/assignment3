from django.contrib import admin

from .models import Available


class AvailableAdmin(admin.ModelAdmin):
    model = Available


admin.site.register(Available, AvailableAdmin)

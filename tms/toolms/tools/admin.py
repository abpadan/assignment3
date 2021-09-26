from django.contrib import admin

from .models import Tool


class ToolAdmin(admin.ModelAdmin):
    model = Tool


admin.site.register(Tool, ToolAdmin)

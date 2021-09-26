from django.contrib import admin

from .models import ToolType


class ToolTypeAdmin(admin.ModelAdmin):
    model = ToolType


admin.site.register(ToolType, ToolTypeAdmin)

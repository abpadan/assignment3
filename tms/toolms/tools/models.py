from django.contrib.auth import get_user_model
from django.db import models

from available.models import Available
from tooltype.models import ToolType
from django.urls import reverse


class Tool(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, default=' ')
    manufacturer = models.CharField(max_length=50, blank=False, null=False, default=' ')
    notes = models.CharField(max_length=200, blank=True, null=True, default=' ')
    available = models.ForeignKey(
        Available,
        on_delete=models.CASCADE,
    )
    type = models.ForeignKey(
        ToolType,
        on_delete=models.CASCADE,
        default=1
    )
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    requested = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('tools_list')

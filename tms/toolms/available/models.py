from django.db import models


class Available(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, default=' ')

    def __str__(self):
        return str(self.name)

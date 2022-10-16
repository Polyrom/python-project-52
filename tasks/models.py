from django.db import models
from django.contrib.auth.models import User
from statuses.models import Statuses


class Tasks(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=3000, blank=True)
    status = models.ForeignKey(Statuses, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author')
    executive = models.ForeignKey(User, on_delete=models.PROTECT, related_name='executive')
    created_at = models.DateTimeField(auto_now_add=True)

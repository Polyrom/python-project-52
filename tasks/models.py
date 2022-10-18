from django.db import models
from django.contrib.auth.models import User
from statuses.models import Status
from labels.models import Label


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=3000, blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True)
    label = models.ManyToManyField(Label, through='Labeled', through_fields=('task', 'label'))
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author')
    executor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='executive')
    created_at = models.DateTimeField(auto_now_add=True)


class Labeled(models.Model):
    task = models.ForeignKey(Task, on_delete=models.PROTECT)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)

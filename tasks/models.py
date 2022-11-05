from django.db import models
from task_manager import settings
from statuses.models import Status
from labels.models import Label


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=3000, blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True)
    labels = models.ManyToManyField(Label,
                                    through='TaskLabels',
                                    through_fields=('task', 'label'),
                                    blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.PROTECT,
                               related_name='author')
    executor = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.PROTECT,
                                 related_name='executive')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TaskLabels(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)

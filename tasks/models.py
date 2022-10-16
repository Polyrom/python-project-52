from django.db import models
from django.contrib.auth.models import User
from statuses.models import Statuses
from labels.models import Labels


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=3000, blank=True)
    status = models.ForeignKey(Statuses, on_delete=models.PROTECT, null=True)
    labels = models.ManyToManyField(Labels, through='Labeled', through_fields=('task', 'label'))
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author')
    executive = models.ForeignKey(User, on_delete=models.PROTECT, related_name='executive')
    created_at = models.DateTimeField(auto_now_add=True)


class Labeled(models.Model):
    task = models.ForeignKey(Task, on_delete=models.PROTECT)
    label = models.ForeignKey(Labels, on_delete=models.PROTECT)

    class Meta:
        db_table = "tasks_task_label"

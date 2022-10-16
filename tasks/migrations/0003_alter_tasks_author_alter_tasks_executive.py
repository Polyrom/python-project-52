# Generated by Django 4.1.2 on 2022-10-16 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0002_tasks_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='executive',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='executive', to=settings.AUTH_USER_MODEL),
        ),
    ]

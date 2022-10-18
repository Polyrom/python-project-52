# Generated by Django 4.1.2 on 2022-10-18 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0004_alter_task_label_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='executor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='executive', to=settings.AUTH_USER_MODEL),
        ),
    ]

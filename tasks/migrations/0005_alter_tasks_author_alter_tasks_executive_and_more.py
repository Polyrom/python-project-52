# Generated by Django 4.1.2 on 2022-10-16 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0004_alter_tasks_author_alter_tasks_executive_and_more'),
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
        migrations.RemoveField(
            model_name='tasks',
            name='status',
        ),
        migrations.AddField(
            model_name='tasks',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='statuses.statuses'),
        ),
    ]

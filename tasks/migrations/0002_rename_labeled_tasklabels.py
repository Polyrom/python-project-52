# Generated by Django 4.1.2 on 2022-11-05 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Labeled',
            new_name='TaskLabels',
        ),
    ]

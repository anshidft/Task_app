# Generated by Django 4.2.5 on 2023-11-05 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_mgt', '0002_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='assignee',
            field=models.CharField(default=1, max_length=85),
            preserve_default=False,
        ),
    ]

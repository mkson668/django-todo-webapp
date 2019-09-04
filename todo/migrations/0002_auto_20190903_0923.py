# Generated by Django 2.1 on 2019-09-03 09:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='dueDate',
        ),
        migrations.AddField(
            model_name='todoitem',
            name='dateCreated',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 3, 9, 23, 39, 867266, tzinfo=utc)),
        ),
    ]

# Generated by Django 4.1.7 on 2023-05-09 14:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='novel',
            name='state',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 9, 14, 46, 33, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='history',
            name='history_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 9, 14, 46, 33, tzinfo=datetime.timezone.utc)),
        ),
    ]

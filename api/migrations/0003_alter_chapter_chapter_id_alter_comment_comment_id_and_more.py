# Generated by Django 4.1.7 on 2023-05-09 15:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_novel_state_alter_comment_created_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='chapter_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 9, 15, 16, 21, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='history',
            name='history_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='history',
            name='history_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 9, 15, 16, 21, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='score',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 4.1.7 on 2023-05-23 07:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_cover_state_alter_comment_created_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 23, 7, 15, 22, tzinfo=datetime.timezone.utc), verbose_name='评论时间'),
        ),
        migrations.AlterField(
            model_name='cover',
            name='state',
            field=models.IntegerField(default=0, verbose_name='推送状态'),
        ),
        migrations.AlterField(
            model_name='history',
            name='history_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 23, 7, 15, 22, tzinfo=datetime.timezone.utc), verbose_name='历史时间'),
        ),
        migrations.AlterField(
            model_name='mail',
            name='mail_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 23, 7, 15, 22, tzinfo=datetime.timezone.utc), verbose_name='邮件时间'),
        ),
    ]

# Generated by Django 4.1.7 on 2023-05-09 12:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('chapter_id', models.IntegerField(primary_key=True, serialize=False)),
                ('chapter_title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('novel_id', models.IntegerField()),
            ],
            options={
                'db_table': 'chapter',
            },
        ),
        migrations.CreateModel(
            name='novel',
            fields=[
                ('novel_id', models.AutoField(primary_key=True, serialize=False)),
                ('novel_title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1023)),
                ('cover', models.CharField(max_length=1023)),
                ('category', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'novel',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255, null=True)),
                ('age', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('favorite', models.IntegerField(null=True)),
                ('score', models.IntegerField(null=True)),
                ('novel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.novel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
            options={
                'db_table': 'score',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('history_id', models.IntegerField(primary_key=True, serialize=False)),
                ('history_time', models.DateTimeField(default=datetime.datetime(2023, 5, 9, 12, 57, 17, tzinfo=datetime.timezone.utc))),
                ('lastchapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.chapter')),
                ('novel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.novel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
            options={
                'db_table': 'history',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('comment_content', models.CharField(max_length=1023)),
                ('created_time', models.DateTimeField(default=datetime.datetime(2023, 5, 9, 12, 57, 17, tzinfo=datetime.timezone.utc))),
                ('novel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.novel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
            options={
                'db_table': 'comment',
            },
        ),
    ]
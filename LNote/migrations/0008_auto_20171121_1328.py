# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-21 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LNote', '0007_auto_20171115_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sharednote',
            name='sharedBy',
        ),
        migrations.RemoveField(
            model_name='sharednote',
            name='status',
        ),
        migrations.RemoveField(
            model_name='sharednote',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='sharednote',
            name='text',
        ),
        migrations.RemoveField(
            model_name='sharednote',
            name='time',
        ),
        migrations.RemoveField(
            model_name='sharednote',
            name='title',
        ),
        migrations.RemoveField(
            model_name='sharednote',
            name='user',
        ),
        migrations.AddField(
            model_name='sharednote',
            name='sharedById',
            field=models.IntegerField(default=False),
        ),
        migrations.AddField(
            model_name='sharednote',
            name='sharedByName',
            field=models.CharField(default=False, max_length=128),
        ),
        migrations.AddField(
            model_name='sharednote',
            name='sharedWithId',
            field=models.IntegerField(default=False),
        ),
    ]

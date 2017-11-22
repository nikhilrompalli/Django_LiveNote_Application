# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-15 07:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LNote', '0003_note_sharedwith'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='sharedWith',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='sharedWith',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]

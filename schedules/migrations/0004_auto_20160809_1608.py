# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-09 07:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0003_auto_20160805_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

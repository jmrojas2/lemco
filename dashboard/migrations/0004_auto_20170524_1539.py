# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-24 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20170524_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work_file',
            name='finish_date_process1',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

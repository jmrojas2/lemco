# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-29 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20170524_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='work_file',
            name='area',
            field=models.CharField(default='-', max_length=10),
        ),
        migrations.AlterField(
            model_name='work_file',
            name='finish_date_process',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='work_file',
            name='number',
            field=models.CharField(max_length=20, verbose_name='Número de Archivo'),
        ),
    ]

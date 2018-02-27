# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-26 14:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galleria', '0004_auto_20180226_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_category',
        ),
        migrations.AddField(
            model_name='image',
            name='image_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='galleria.Category'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 06:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20160824_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='block.Block', verbose_name='版块ID'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 02:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='block.Block', verbose_name='版块ID'),
        ),
    ]

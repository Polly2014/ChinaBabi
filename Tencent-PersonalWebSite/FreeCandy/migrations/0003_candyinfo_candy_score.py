# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-05-19 05:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FreeCandy', '0002_auto_20180519_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='candyinfo',
            name='candy_score',
            field=models.IntegerField(default=10, verbose_name='Candy Reputation'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-05 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UCAS_DM', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='id',
        ),
        migrations.AddField(
            model_name='document',
            name='document_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]

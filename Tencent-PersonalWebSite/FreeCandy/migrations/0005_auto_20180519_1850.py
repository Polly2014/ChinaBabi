# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-05-19 10:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('FreeCandy', '0004_auto_20180519_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecieveInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_phone', models.CharField(max_length=15, verbose_name='Phone Number')),
                ('guest_wallet', models.CharField(max_length=64, verbose_name='Wallet Address')),
                ('candy_name', models.CharField(max_length=50, verbose_name='Candy Name')),
                ('candy_amount', models.CharField(max_length=50, verbose_name='Candy Amount')),
                ('recieve_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Recieve Time')),
            ],
        ),
        migrations.AlterField(
            model_name='candyinfo',
            name='candy_flag',
            field=models.BooleanField(default=False, verbose_name='Candy Online'),
        ),
        migrations.AlterField(
            model_name='candyinfo',
            name='candy_link',
            field=models.CharField(default='freeCandyDetail/?candy_name=', max_length=200, verbose_name='Candy Link'),
        ),
        migrations.AlterField(
            model_name='candyinfo',
            name='candy_score',
            field=models.IntegerField(default=10, verbose_name='Candy Reputation'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-06-12 10:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BabiCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_address', models.CharField(max_length=100, verbose_name='Company Adress')),
                ('company_flag', models.IntegerField(default=0, verbose_name='Babi Flag')),
            ],
        ),
        migrations.CreateModel(
            name='BabiTrainee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('babi_id', models.CharField(blank=True, max_length=60, null=True, verbose_name='Babi ID')),
                ('babi_train_count', models.IntegerField(default=12, verbose_name='Babi Train Count')),
                ('babi_photo', models.CharField(default='/static/img/babi_default.png', max_length=200, verbose_name='Babi Photo')),
                ('babi_role', models.IntegerField(choices=[(0, '\u65e0'), (1, '\u4e3b\u5531'), (2, '\u9886\u5531'), (3, '\u526f\u4e3b\u5531'), (4, '\u4e3b\u821e'), (5, '\u9886\u821e'), (6, '\u4e3bRapper'), (7, '\u526fRapper'), (8, 'Center')], default=0, verbose_name='Babi Role')),
                ('babi_skill_sing', models.IntegerField(default=0, verbose_name='Sing Score')),
                ('babi_skill_dancing', models.IntegerField(default=0, verbose_name='Dancing Score')),
                ('babi_skill_acting', models.IntegerField(default=0, verbose_name='Acting Score')),
                ('babi_flag', models.IntegerField(default=0, verbose_name='Babi Flag')),
            ],
        ),
        migrations.AddField(
            model_name='babicompany',
            name='company_babi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BabiInfo', to='BabiGame.BabiTrainee', verbose_name='Babi Info'),
        ),
    ]
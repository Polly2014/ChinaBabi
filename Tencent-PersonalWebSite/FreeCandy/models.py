# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import django.utils.timezone as timezone
from random import randint

# Create your models here.

class CandyInfo(models.Model):
	candy_name = models.CharField('Candy Name', max_length=50)
	candy_type = models.CharField('Candy Type', max_length=50, null=True,blank=True)
	candy_amount = models.IntegerField('Candy Amount')
	candy_score = models.IntegerField('Candy Reputation', default=randint(0,10))
	candy_link = models.CharField('Candy Link', max_length=200, default='freeCandyDetail/?candy_name=')
	candy_logo = models.CharField('Candy Logo', max_length=200, default='/static/img/pic_small.jpg')
	candy_note = models.CharField('Candy Note', max_length=50, null=True,blank=True)
	candy_flag = models.BooleanField('Candy Online', default=False)
	
	def __unicode__(self):
		return '{} [{}]'.format(self.candy_name, self.candy_note)

class RecieveInfo(models.Model):
	guest_phone = models.CharField('Phone Number', max_length=15)
	guest_wallet = models.CharField('Wallet Address', max_length=64)
	candy_name = models.CharField('Candy Name', max_length=50)
	candy_amount = models.IntegerField('Candy Amount')
	recieve_time = models.DateTimeField('Recieve Time', default=timezone.now)

	def __unicode__(self):
		return '{}-{}-{}'.format(self.guest_phone, self.candy_name, self.recieve_time)


# class 

'''
<p class="card-param-1">Epnex</p>
<p class="card-param-2">NEO</p>
<div class="info">
	<h2 class="card-title">EPN</h2>
	<p class="card-description">交易所</p>
</div>
'''
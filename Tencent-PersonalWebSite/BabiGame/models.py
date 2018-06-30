# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import json

# Create your models here.
class BabiTrainee(models.Model):
	BABI_ROLE = ((0, u'普通'), (1, u'主唱'), (2, u'领唱'),(3, u'副主唱'), \
		(4, u'主舞'), (5, u'领舞'), (6, u'主Rapper'), (7, u'副Rapper'), (8, u'Center'),)
	BABI_SKILL = json.dumps({'score':0, 'trainedList':[]})
	babi_id = models.CharField('Babi ID', max_length=60, blank=True, null=True)
	babi_train_count = models.IntegerField('Babi Train Count', default=12)
	babi_photo = models.CharField('Babi Photo', max_length=200, default='/static/img/babi_0.png')
	babi_role = models.IntegerField('Babi Role', choices=BABI_ROLE, default=0)
	babi_skill_sing = models.CharField('Sing Skill', max_length=300, default=BABI_SKILL)
	babi_skill_dancing = models.CharField('Dancing Skill', max_length=300, default=BABI_SKILL)
	babi_skill_acting = models.CharField('Acting Skill', max_length=300, default=BABI_SKILL)
	babi_flag = models.IntegerField('Babi Flag', default=0)

	def __unicode__(self):
		return '[{}]-{}'.format(self.id, self.babi_id)

class BabiCompany(models.Model):
	company_address = models.CharField('Company Address', max_length=100)
	company_babi = models.ForeignKey(BabiTrainee, verbose_name='Babi Info', related_name='BabiInfo')
	company_flag = models.IntegerField('Company Flag', default=0)

	def __unicode__(self):
		return '[{}]-{}'.format(self.company_flag, self.company_address)

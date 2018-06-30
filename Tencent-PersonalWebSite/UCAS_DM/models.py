# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import django.utils.timezone as timezone

# Create your models here.

class Document(models.Model):
	document_id = models.AutoField('文档ID', primary_key=True)
	location_from = models.CharField('来文单位', max_length=50)
	valid_code = models.CharField('文档查验码', max_length=20)
	document_code = models.CharField('文档条码号', max_length=10, blank=True, null=True)
	title = models.CharField('标题摘要', max_length=200)
	time_recieve = models.DateTimeField('录入时间', default=timezone.now)
	
	def __unicode__(self):
		return '[{}]-{}'.format(self.document_id, self.title)

	class Meta:
		verbose_name = u'公文文档信息'
		verbose_name_plural = verbose_name

class Record(models.Model):
	document_info = models.ForeignKey(Document, verbose_name='文档信息', related_name='DocumentInfo')
	time_forward = models.DateTimeField('转发时间', default=timezone.now)
	location_to = models.CharField('转发去向', max_length=50)
	time_recycle = models.DateTimeField('回收时间', blank=True, null=True)
	opinion_leader = models.CharField('领导意见', max_length=100)
	
	def __unicode__(self):
		return '{} [{}]'.format(self.document_info, self.opinion_leader)
		
	class Meta:
		verbose_name = u'公文流转信息'
		verbose_name_plural = verbose_name

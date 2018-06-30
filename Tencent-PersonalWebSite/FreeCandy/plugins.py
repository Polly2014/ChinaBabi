# -*- coding: utf-8 -*-
from django.utils import timezone
import time, json

ISOTIMEFORMAT = '%Y-%m-%d %H:%M'

def timeFormat(time_db):
	return timezone.localtime(time_db).strftime(ISOTIMEFORMAT)

def validTimePeriod(recieve_time):
	now = timezone.now()
	return True if (now-timezone.localtime(recieve_time)).seconds>24*60*60 else False

def getAccountInfo(accountQuerySet):
	result = []
	for account in accountQuerySet:
		candy_name = account.candy_name
		candy_amount = account.candy_amount
		recieve_time = account.recieve_time
		item = {
			'candy_name': candy_name, 
			'candy_amount': candy_amount,
			'recieve_time': timeFormat(recieve_time)
		}
		result.append(item)	
	return result

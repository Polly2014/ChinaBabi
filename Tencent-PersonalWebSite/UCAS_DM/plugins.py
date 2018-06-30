# -*- coding: utf-8 -*-
from django.utils import timezone
import time

ISOTIMEFORMAT = '%Y-%m-%d %H:%M'

def timeFormat(time_db):
	return timezone.localtime(time_db).strftime(ISOTIMEFORMAT)

def getDetailInfo(documentInfo, recordList):
	DocumentInfo = {
		'id': documentInfo.document_id,
		'title': documentInfo.title,
		'location_from': documentInfo.location_from,
		'time_recieve': timeFormat(documentInfo.time_recieve)
	}
	RecordInfo = {'History':[], 'Current':{}}
	if recordList:
		for record in recordList:
			item = {
				'time_forward': timeFormat(record.time_forward),
				'location_to': record.location_to,
				'time_recycle': timeFormat(record.time_recycle),
				'opinion_leader': record.opinion_leader
			}
			RecordInfo['History'].append(item)
		record = recordList[-1]
		RecordInfo['Current'] = {
			'time_forward': timeFormat(record.time_forward),
			'location_to': record.location_to,
			'time_recycle': timeFormat(record.time_recycle),
			'opinion_leader': record.opinion_leader
		}
	return {'DocumentInfo':DocumentInfo, 'RecordInfo':RecordInfo}
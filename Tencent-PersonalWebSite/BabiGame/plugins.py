# -*- coding: utf-8 -*-
# import os, django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PersonalWebSite.settings")
# django.setup()

from django.utils import timezone
from models import *
from random import randint
import time, json

ISOTIMEFORMAT = '%Y-%m-%d %H:%M'
NAME = {'YL':u'乐理', 'JQ':u'唱歌技巧', 'DC':u'独唱', 'HY':u'和音', 'HC':u'合唱', \
	'TN':u'体能', 'XT':u'形体', 'DW':u'独舞', 'QW':u'齐舞', 'JX':u'即兴舞蹈',\
	'RAP':u'RAP', 'CZ':u'唱作', 'TF':u'台风', 'ZY':u'综艺感', 'BQ':u'表情管理'}
SKILL = {
	'YL': [8, 5, 3, 1],
	'JQ': [8, 5, 3, 1],
	'DC': [[8, 5, 3, 3], [5, 3, 3, 3]],
	'HY': [[8, 5, 3, 3], [5, 3, 3, 3]],
	'HC': [[8, 5, 3, 3], [5, 3, 3, 3]],
	'TN': [8, 5, 3, 1],
	'XT': [8, 5, 3, 1],
	'DW': [[8, 5, 3, 3], [5, 5, 3, 3]],
	'QW': [[8, 5, 3, 3], [5, 5, 3, 3]],
	'JX': [[8, 5, 3, 5], [5, 5, 3, 5]],
	'RAP': [10, 5, 3, 1],
	'CZ': [[10, 5, 3, 1], [5, 5, 3, 1]],
	'TF': [1.25, 5, 3, 1],
	'ZY': [8, 8, 3, 1],
	'BQ': [8, 5, 3, 1]
}

def countNumberOfTrained(skill, trainedList):
	return sum([1 if t[0]==skill else 0 for t in trainedList])

def isSkillHasTrained(skill, trainedList):
	return True if [skill, SKILL[skill][0]] in trainedList else False

def babiRoleEvaluate(skillDict):
	score_sing = skillDict['sing']['score']
	score_dancing = skillDict['dancing']['score']
	score_acting = skillDict['acting']['score']
	actingTrainedList = skillDict['acting']['trainedList']
	if score_sing>=35 and score_dancing>=35 and score_acting>=15:
		return 8, u'Center'
	elif score_sing>=35 and score_dancing>=0 and score_acting>=0:
		return 1, u'主唱'
	elif score_sing>=30 and score_dancing>=0 and score_acting>=0:
		return 2, u'领唱'
	elif score_sing>=25 and score_dancing>=0 and score_acting>=0:
		return 3, u'副主唱'
	elif score_sing>=0 and score_dancing>=35 and score_acting>=0:
		return 4, u'主舞'
	elif score_sing>=0 and score_dancing>=30 and score_acting>=0:
		return 5, u'领舞'
	elif score_sing>=0 and score_dancing>=0 and ['RAP',3] in actingTrainedList:
		return 6, u'主Rapper'
	elif score_sing>=0 and score_dancing>=0 and ['RAP',5] in actingTrainedList:
		return 7, u'副Rapper'
	else:
		return 0, u'普通'

def initBabiInfo(babi_session):
	babi = BabiTrainee()
	# babi.save()
	skill_dict = {'sing':json.loads(babi.babi_skill_sing),
		'dancing':json.loads(babi.babi_skill_dancing),
		'acting':json.loads(babi.babi_skill_acting)}
	babiInfo = {'id':babi.id, 'adress':babi.babi_id,'count':babi.babi_train_count, \
		'photo':babi.babi_photo, 'role':babi.get_babi_role_display(), 'role_no':babi.babi_role, \
		'skills':skill_dict, 'flag':babi.babi_flag, 'babi_session':babi_session, 'tips':''}
	return babiInfo

def updateBabiInfo(babiInfo, option):
	if babiInfo['count']>0:
		if option in ['YL', 'JQ']:
			trainedScore = babiInfo['skills']['sing']['score']
			trainedList = babiInfo['skills']['sing']['trainedList']
			num = countNumberOfTrained(option, trainedList)
			num = -1 if num>3 else num
			babiInfo['skills']['sing']['trainedList'].append([option, SKILL[option][num]])
			babiInfo['skills']['sing']['score'] += SKILL[option][num]
			babiInfo['skills']['sing']['score'] = babiInfo['skills']['sing']['score'] if babiInfo['skills']['sing']['score']<=40 else 40
			score = babiInfo['skills']['sing']['score'] - trainedScore
			if score>0:
				babiInfo['tips'] = u'{}训练成功，声乐评分+{}分！'.format(NAME[option], score)
			else:
				babiInfo['tips'] = u'声乐已训练至满分！'
		elif option in ['DC', 'HY', 'HC']:
			trainedScore = babiInfo['skills']['sing']['score']
			trainedList = babiInfo['skills']['sing']['trainedList']
			flag = 0 if isSkillHasTrained('YL', trainedList) else 1
			num = countNumberOfTrained(option, trainedList)
			num = -1 if num>3 else num
			babiInfo['skills']['sing']['trainedList'].append([option, SKILL[option][flag][num]])
			babiInfo['skills']['sing']['score'] += SKILL[option][flag][num]
			babiInfo['skills']['sing']['score'] = babiInfo['skills']['sing']['score'] if babiInfo['skills']['sing']['score']<=40 else 40
			score = babiInfo['skills']['sing']['score'] - trainedScore
			if score>0:
				babiInfo['tips'] = u'{}训练成功，声乐评分+{}分！'.format(NAME[option], score)
			else:
				babiInfo['tips'] = u'声乐已训练至满分！'
		elif option in ['TN', 'XT']:
			trainedScore = babiInfo['skills']['dancing']['score']
			trainedList = babiInfo['skills']['dancing']['trainedList']
			num = countNumberOfTrained(option, trainedList)
			num = -1 if num>3 else num
			babiInfo['skills']['dancing']['trainedList'].append([option, SKILL[option][num]])
			babiInfo['skills']['dancing']['score'] += SKILL[option][num]
			babiInfo['skills']['dancing']['score'] = babiInfo['skills']['dancing']['score'] if babiInfo['skills']['dancing']['score']<=40 else 40
			score = babiInfo['skills']['dancing']['score'] - trainedScore
			if score>0:
				babiInfo['tips'] = u'{}训练成功，舞蹈评分+{}分！'.format(NAME[option], score)
			else:
				babiInfo['tips'] = u'舞蹈已训练至满分！'
		elif option in ['DW', 'QW', 'JX']:
			trainedScore = babiInfo['skills']['dancing']['score']
			trainedList = babiInfo['skills']['dancing']['trainedList']
			flag = 0 if isSkillHasTrained('XT', trainedList) else 1
			num = countNumberOfTrained(option, trainedList)
			num = -1 if num>3 else num
			babiInfo['skills']['dancing']['trainedList'].append([option, SKILL[option][flag][num]])
			babiInfo['skills']['dancing']['score'] += SKILL[option][flag][num]
			babiInfo['skills']['dancing']['score'] = babiInfo['skills']['dancing']['score'] if babiInfo['skills']['dancing']['score']<=40 else 40
			score = babiInfo['skills']['dancing']['score'] - trainedScore
			if score>0:
				babiInfo['tips'] = u'{}训练成功，舞蹈评分+{}分！'.format(NAME[option], score)
			else:
				babiInfo['tips'] = u'舞蹈已训练至满分！'
		elif option in ['RAP', 'ZY', 'BQ']:
			trainedScore = babiInfo['skills']['acting']['score']
			trainedList = babiInfo['skills']['acting']['trainedList']
			num = countNumberOfTrained(option, trainedList)
			num = -1 if num>3 else num
			babiInfo['skills']['acting']['trainedList'].append([option, SKILL[option][num]])
			babiInfo['skills']['acting']['score'] += SKILL[option][num]
			babiInfo['skills']['acting']['score'] = babiInfo['skills']['acting']['score'] if babiInfo['skills']['acting']['score']<=20 else 20
			score = babiInfo['skills']['acting']['score'] - trainedScore
			if score>0:
				babiInfo['tips'] = u'{}训练成功，艺能评分+{}分！'.format(NAME[option], score)
			else:
				babiInfo['tips'] = u'艺能已训练至满分！'
		elif option=='CZ':
			trainedScore = babiInfo['skills']['acting']['score']
			trainedList = babiInfo['skills']['acting']['trainedList']
			flag = 0 if isSkillHasTrained('YL', trainedList) else 1
			num = countNumberOfTrained(option, trainedList)
			num = -1 if num>3 else num
			babiInfo['skills']['acting']['trainedList'].append([option, SKILL[option][flag][num]])
			babiInfo['skills']['acting']['score'] += SKILL[option][flag][num]
			babiInfo['skills']['acting']['score'] = babiInfo['skills']['acting']['score'] if babiInfo['skills']['acting']['score']<=20 else 20
			score = babiInfo['skills']['acting']['score'] - trainedScore
			if score>0:
				babiInfo['tips'] = u'{}训练成功，艺能评分+{}分！'.format(NAME[option], score)
			else:
				babiInfo['tips'] = u'艺能已训练至满分！'
		elif option=='TF':
			trainedScore = babiInfo['skills']['acting']['score']
			trainedList = babiInfo['skills']['acting']['trainedList']
			num = countNumberOfTrained(option, trainedList)
			num = -1 if num>3 else num
			score = SKILL[option][num]*(babiInfo['skills']['sing']['score']+\
				babiInfo['skills']['dancing']['score']) if num==0 else SKILL[option][num]
			babiInfo['skills']['acting']['trainedList'].append([option, score])
			babiInfo['skills']['acting']['score'] += score
			babiInfo['skills']['acting']['score'] = babiInfo['skills']['acting']['score'] if babiInfo['skills']['acting']['score']<=20 else 20
			score = babiInfo['skills']['acting']['score'] - trainedScore
			if score>0 or babiInfo['skills']['acting']['score']<=20:
				babiInfo['tips'] = u'{}训练成功，艺能评分+{}分！'.format(NAME[option], score)
			else:
				babiInfo['tips'] = u'艺能已训练至满分！'
		else:
			pass
		babiInfo['count'] -=1
		skillDict = babiInfo['skills']
		babiInfo['role_no'], babiInfo['role'] = babiRoleEvaluate(skillDict)
		babiInfo['photo'] = '/static/img/babi_{}.png'.format(babiInfo['role_no'])
		# if option=='sing':
		# 	babiInfo['skills']['sing'] += randint(1,10)
		# 	print "Sing Skill Increase!"
		# elif option=='dancing':
		# 	babiInfo['skills']['dancing'] += randint(1,10)
		# elif option=='acting':
		# 	babiInfo['skills']['acting'] += randint(1,10)
		# elif option=='lucky':
		# 	babiInfo['skills']['sing'] += randint(1,4)
		# 	babiInfo['skills']['dancing'] += randint(1,4)
		# 	babiInfo['skills']['acting'] += randint(1,4)
		# else:
		# 	pass
	else:
		babiInfo['count'] = 0
		babiInfo['tips'] = u'训练次数已用完'
	return babiInfo

def evaluateBabiInfo(babiInfo):
	score = sum([skill['score'] for _,skill in babiInfo['skills'].items()])
	if score>80:
		babiInfo['tips'] = u'太棒啦，非常有做偶像的潜质呢！'
	elif score>70:
		babiInfo['tips'] = u'很有做练习生的潜质呢！'
	elif score>60:
		babiInfo['tips'] = u'具备了做练习生的基本条件！'
	elif score>50:
		babiInfo['tips'] = u'加油，在努力一点！'
	elif score>40:
		babiInfo['tips'] = u'别灰心，还有机会！'
	elif score>20:
		babiInfo['tips'] = u'成绩还不是很理想呢！'
	else:
		babiInfo['tips'] = u'并不适合做练习生呢>_<'
	return babiInfo

def formatBabiInfo(babi):
	skill_dict = {'sing':json.loads(babi.babi_skill_sing),
		'dancing':json.loads(babi.babi_skill_dancing),
		'acting':json.loads(babi.babi_skill_acting)}
	babiInfo = {'id':babi.id, 'adress':babi.babi_id,'count':babi.babi_train_count, \
		'photo':babi.babi_photo, 'role':babi.get_babi_role_display(), 'role_no':babi.babi_role, \
		'skills':skill_dict, 'flag':babi.babi_flag, 'tips':''}
	return babiInfo

def saveBabiInfo(babiInfo):
	result = {'code':1, 'msg':'Save BabiInfo Success!'}
	try:
		babiQuerySet = BabiTrainee.objects.filter(babi_id=babiInfo['babi_session'])
		if babiQuerySet.exists():
			result['msg'] = u'您已成功签约该练习生，无需反复提交！'
			return result
		else:
			babi = BabiTrainee(
				babi_id=babiInfo['babi_session'],
				babi_train_count=babiInfo['count'], babi_photo=babiInfo['photo'], babi_role=babiInfo['role_no'],\
				babi_skill_sing=json.dumps(babiInfo['skills']['sing']),\
				babi_skill_dancing=json.dumps(babiInfo['skills']['dancing']),\
				babi_skill_acting=json.dumps(babiInfo['skills']['acting']), babi_flag=1)
			babi.save()
			print "########{}".format(babi.id)
			result['code'] = 0
			result['msg'] = formatBabiInfo(BabiTrainee.objects.filter(babi_id=babiInfo['babi_session'])[0])
	except Exception, e:
		result['msg'] = 'Save BabiInfo Error, Because {}'.format(e)
	return result

def saveCompanyInfo(company_address, babi_session):
	result = {'code':1, 'msg':'Save CompanyInfo Success!'}
	try:
		babiInfo = BabiTrainee.objects.filter(babi_id=babi_session)
		if babiInfo.exists():
			company = BabiCompany(company_address=company_address, company_babi=babiInfo[0], company_flag=1)
			company.save()
			result['code'] = 0
		else:
			result['msg'] = 'Save CompanyInfo Error, BabiInfo Not Exists!'
	except Exception, e:
		result['msg'] = 'Save CompanyInfo Error, Because {}'.format(e)
	return result

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
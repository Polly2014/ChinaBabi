# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from models import CandyInfo, RecieveInfo
from random import randint
from django.utils import timezone
import plugins, json
import uuid, re
# Create your views here.

RULE_PHONE = r'[0-9]{11}'

def fc_index(request):
	# return HttpResponse("Hello, Free Candy!")
	candyList = CandyInfo.objects.filter(candy_flag=True).order_by('-candy_score')
	return render_to_response('index.html', {"errors":"None", "candyList": candyList})

@csrf_exempt
def fc_publish(request):
	return render_to_response('publish.html', {})

@csrf_exempt
def fc_publishFreeCandy(request):
	result = {'code':1, 'message': u'Free Candy已提交成功，请耐心等待审核通过!'}
	if request.method=='POST':
		candy_name = request.POST.get('candy_name', '')
		candy_type = request.POST.get('candy_type', '')
		candy_amount = request.POST.get('candy_amount', 0)
		candy_link = request.POST.get('candy_link', '')
		candy_link = candy_link if candy_link else 'freeCandyDetail/?candy_name='
		candy_note = request.POST.get('candy_note', '')
		candyQuerySet = CandyInfo.objects.filter(candy_name=candy_name, candy_type=candy_type)
		if candyQuerySet.exists():
			result['message'] = 'Free Candy Already Exists!'
		else:
			candy = CandyInfo(candy_name=candy_name, candy_type=candy_type, candy_amount=candy_amount,\
				candy_link=candy_link, candy_note=candy_note)
			candy.save()
			result['code'] = 0
	else:
		result['message'] = 'Only Support POST Method!'
	print result
	return HttpResponse(json.dumps(result))

def fc_freeCandyDetail(request):
	candy_name = request.GET.get('candy_name', '')
	if candy_name:
		return render_to_response('freeCandyDetail.html', {'candy_name': candy_name})
	else:
		return HttpResponseRedirect('/freecandy/')

@csrf_exempt
def fc_validGuestInfo(request):
	result = {'code':1, 'message':'Valid Guest Info Success!'}
	guest_phone = request.POST.get('guest_phone', '')
	candy_name = request.POST.get('candy_name', '')

	m = re.match(RULE_PHONE, guest_phone)
	if not m:
		result['message'] = u'手机格式错误，请重新填写!'
		return HttpResponse(json.dumps(result))

	candy = CandyInfo.objects.filter(candy_name=candy_name)[0]
	if candy.candy_amount<=0:
		result['message'] = 'Sorry, There\'s No Free Candy!'
		return HttpResponse(json.dumps(result))

	RecieveQuerySet = RecieveInfo.objects.filter(guest_phone=guest_phone)
	if RecieveQuerySet.exists():
		recieve = RecieveQuerySet[0]
		guest_wallet = recieve.guest_wallet
		candy_amount = randint(1, min(candy.candy_amount, 20))
		result['code'] = 0
		result['message'] = {'guest_wallet':guest_wallet, 'candy_amount':candy_amount}
	else:
		guest_wallet = str(uuid.uuid1())
		candy_amount = randint(1, min(candy.candy_amount, 20))
		result['code'] = 2
		result['message'] = {'guest_wallet':guest_wallet, 'candy_amount':candy_amount}
	return HttpResponse(json.dumps(result))

@csrf_exempt
def fc_getFreeCandy(request):
	result = {'code':1, 'message':'Get Free Candy Success!'}
	guest_phone = request.POST.get('guest_phone', '')
	guest_wallet = request.POST.get('guest_wallet', '')
	candy_name = request.POST.get('candy_name', '')
	candy_amount = int(request.POST.get('candy_amount', 0))

	RecieveQuerySet = RecieveInfo.objects.filter(guest_phone=guest_phone, candy_name=candy_name)
	if RecieveQuerySet.exists():
		recieve = RecieveQuerySet[0]
		if plugins.validTimePeriod(recieve.recieve_time):
			RecieveQuerySet.update(candy_amount=candy_amount+recieve.candy_amount, recieve_time=timezone.now())
			result['code'] = 0
			accountQuerySet = RecieveInfo.objects.filter(guest_phone=guest_phone)
			result['message'] = plugins.getAccountInfo(accountQuerySet)
		else:
			result['message']  = u'24小时内无法重复领取'
	else:
		recieve = RecieveInfo(guest_phone=guest_phone, guest_wallet=guest_wallet,\
			candy_name=candy_name, candy_amount=candy_amount)
		recieve.save()
		result['code'] = 0
		accountQuerySet = RecieveInfo.objects.filter(guest_phone=guest_phone)
		result['message'] = plugins.getAccountInfo(accountQuerySet)
	return HttpResponse(json.dumps(result))


# @csrf_exempt
# def dm_valid(request):
# 	if request.method=='POST':
# 		documentID = int(request.POST.get('documentID', 0))
# 		documentCode = request.POST.get('documentCode', '')
# 		documentInfo = Document.objects.filter(document_id=documentID, valid_code=documentCode)
# 		if documentInfo.exists():
# 			pass
# 		return HttpResponse("True if documentInfo.exists() else False")
# 	else:
# 		return HttpResponse("Only Support POST Method")

# @csrf_exempt
# def dm_search(request):
# 	documentID = int(request.POST.get('documentID', 0))
# 	documentCode = request.POST.get('documentCode', '')

# 	documentInfo = Document.objects.filter(document_id=documentID, valid_code=documentCode)
# 	if documentInfo.exists():
# 		recordList = list(Record.objects.filter(document_info=documentInfo).all())
# 		recordLast = recordList[-1]
# 		return HttpResponse('DocumentID or ValidCode Right!')
# 	else:
# 		return HttpResponse('DocumentID or ValidCode Wrong!')
# 		# return render_to_response('login.html', {"errors":errors})

# @csrf_exempt
# def dm_getDetailInfo(request):
# 	documentID = int(request.GET.get('documentID', 0))
# 	documentCode = request.GET.get('documentCode', '')

# 	documentInfo = Document.objects.filter(document_id=documentID, valid_code=documentCode)
# 	if documentInfo.exists():
# 		recordList = list(Record.objects.filter(document_info=documentInfo[0]).all())
# 		result = plugins.getDetailInfo(documentInfo[0], recordList)
# 		return HttpResponse(json.dumps(result))
# 	else:
# 		return HttpResponse('DocumentID or ValidCode Wrong!')

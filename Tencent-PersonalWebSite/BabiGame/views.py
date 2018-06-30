# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import plugins, json, uuid
# Create your views here.

def babi_index(request):
	# return HttpResponse("Hello, UCAS Document Manager!")
	return render_to_response('babi_index.html', {"errors":"None"})
	# return HttpResponse('Hi Babi Game!')

def babi_foster(request):
	request.session['babi_session'] = str(uuid.uuid1())
	return render_to_response('babi_foster.html')

#------------------- Call For Plugins --------------------------#

def initBabiInfo(request):
	result = {'code':0, 'msg':''}
	babi_session = request.session['babi_session'] if request.session['babi_session'] else str(uuid.uuid1())
	try:
		babiInfo = plugins.initBabiInfo(babi_session)
		request.session['babi_info'] = json.dumps(babiInfo)
		result['msg'] = babiInfo
	except Exception, e:
		result['msg'] = 'Init BabiInfo Error, Because {}'.format(e)
	return HttpResponse(json.dumps(result))

def updateBabiInfo(request):
	result = {'code':0, 'msg':'Update BabiInfo Error!'}
	option = request.GET.get('option', '')
	if option:
		babiInfo = json.loads(request.session['babi_info'])
		babiInfo = plugins.updateBabiInfo(babiInfo, option)
		if babiInfo['count']==0:
			result['code'] = 2
		result['msg'] = babiInfo
		request.session['babi_info'] = json.dumps(babiInfo)
	else:
		result['code'] = 1
	# print json.dumps(result)
	return HttpResponse(json.dumps(result))

def saveBabiInfo(request):
	result = {'code':0, 'msg':'Save BabiInfo Error!'}
	try:
		babiInfo = json.loads(request.session['babi_info'])
		if not babiInfo['count']==0:
			result['code'] = 2
			result['msg'] = 'Save BabiInfo Error! Because of Trained Count is Not Zero'
			return HttpResponse(json.dumps(result))
		result = plugins.saveBabiInfo(babiInfo)
	except Exception, e:
		result['code'] = 1
		result['msg'] = 'Save BabiInfo Error! Because of {}-{}'.format(Exception, e)
	return HttpResponse(json.dumps(result))

@csrf_exempt
def saveCompanyInfo(request):
	result = {'code':0, 'msg':'Save BabiInfo Error!'}
	try:
		company_address = request.POST.get('company_address', '')
		babi_session = request.POST.get('babi_session', '')
		print "###{}-{}".format(company_address, babi_session)
		if company_address and babi_session:
			result = plugins.saveCompanyInfo(company_address, babi_session)
		else:
			result['msg'] = 'Save BabiInfo Error! BabiInfo or CompanyInfo is Null!'
	except Exception, e:
		result['code'] = 1
		result['msg'] = 'Save BabiInfo Error! Because of {}-{}'.format(Exception, e)
	return HttpResponse(json.dumps(result))

def evaluateBabiInfo(request):
	result = {'code':0, 'msg':'Evaluate BabiInfo Error!'}
	try:
		babiInfo = json.loads(request.session['babi_info'])
		babiInfo = plugins.evaluateBabiInfo(babiInfo)
		result['msg'] = babiInfo['tips']
	except Exception,e:
		result['code'] = 1
		result['msg'] = 'Evaluate BabiInfo Error! Because of {}'.format(e)
	return HttpResponse(json.dumps(result))
	# pass
	# return render_to_response('evalueBabiInfo.html')

# @csrf_exempt
# def dm_detail(request):
# 	documentID = int(request.POST.get('documentID', 0))
# 	documentCode = request.POST.get('documentCode', '')
# 	return render_to_response('detailInfo.html', locals())

# @csrf_exempt
# def dm_valid(request):
# 	result = {'code':1, 'message': 'Valid Success!'}
# 	if request.method=='POST':
# 		documentID = int(request.POST.get('documentID', 0))
# 		documentCode = request.POST.get('documentCode', '')
# 		documentInfo = Document.objects.filter(document_id=documentID, valid_code=documentCode)
# 		result['code'] = 0 if documentInfo.exists() else 1
# 		result['message'] = u'文档序号或验证码错误，请重新输入!' if result['code'] else result['message']
# 	else:
# 		result['message'] = 'Only POST Method Support!'
# 	return HttpResponse(json.dumps(result))

# @csrf_exempt
# def dm_showDocumentInfo(request):
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


# def dm_getDetailInfo(request):
# 	result = {'code':1, 'message':'Document Not Exists!'}
# 	documentID = int(request.GET.get('documentID', 0))
# 	documentCode = request.GET.get('documentCode', '')

# 	documentInfo = Document.objects.filter(document_id=documentID, valid_code=documentCode)
# 	if documentInfo.exists():
# 		recordList = list(Record.objects.filter(document_info=documentInfo).all())
# 		result['code'] = 0 if recordList else 2
# 		result['message'] = plugins.getDetailInfo(documentInfo[0], recordList)
# 	return HttpResponse(json.dumps(result))

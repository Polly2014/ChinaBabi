# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from models import Document, Record
import plugins, json
# Create your views here.

def dm_index(request):
	# return HttpResponse("Hello, UCAS Document Manager!")
	return render_to_response('index_new.html', {"errors":"None"})

@csrf_exempt
def dm_detail(request):
	documentID = int(request.POST.get('documentID', 0))
	documentCode = request.POST.get('documentCode', '')
	return render_to_response('detailInfo.html', locals())

@csrf_exempt
def dm_valid(request):
	result = {'code':1, 'message': 'Valid Success!'}
	if request.method=='POST':
		documentID = int(request.POST.get('documentID', 0))
		documentCode = request.POST.get('documentCode', '')
		documentInfo = Document.objects.filter(document_id=documentID, valid_code=documentCode)
		result['code'] = 0 if documentInfo.exists() else 1
		result['message'] = u'文档序号或验证码错误，请重新输入!' if result['code'] else result['message']
	else:
		result['message'] = 'Only POST Method Support!'
	return HttpResponse(json.dumps(result))

@csrf_exempt
def dm_showDocumentInfo(request):
	documentID = int(request.POST.get('documentID', 0))
	documentCode = request.POST.get('documentCode', '')

	documentInfo = Document.objects.filter(document_id=documentID, valid_code=documentCode)
	if documentInfo.exists():
		recordList = list(Record.objects.filter(document_info=documentInfo).all())
		recordLast = recordList[-1]
		return HttpResponse('DocumentID or ValidCode Right!')
	else:
		return HttpResponse('DocumentID or ValidCode Wrong!')
		# return render_to_response('login.html', {"errors":errors})


def dm_getDetailInfo(request):
	result = {'code':1, 'message':'Document Not Exists!'}
	documentID = int(request.GET.get('documentID', 0))
	documentCode = request.GET.get('documentCode', '')

	documentInfo = Document.objects.filter(document_id=documentID, valid_code=documentCode)
	if documentInfo.exists():
		recordList = list(Record.objects.filter(document_info=documentInfo).all())
		result['code'] = 0 if recordList else 2
		result['message'] = plugins.getDetailInfo(documentInfo[0], recordList)
	return HttpResponse(json.dumps(result))

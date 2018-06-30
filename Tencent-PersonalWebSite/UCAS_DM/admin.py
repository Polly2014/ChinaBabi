# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *
# Register your models here.
	
class RecordInfoInline(admin.TabularInline):
	model = Record

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
	inlines = [RecordInfoInline,]
	list_display = ('document_id', 'location_from', 'valid_code', 'document_code', 'title', 'time_recieve',)
	search_fields = ('document_id', 'title',)
	# fk_fields = ('location_from', 'time_forward', 'location_to', 'time_recycle', 'opinion_leader',)

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
	list_display = ('document_info', 'time_forward', 'location_to', 'time_recycle', 'opinion_leader',)
	search_fields = ('location_to', 'opinion_leader',)
	# fk_fields = ('location_from',)

# admin.site.register(Document, DocumentAdmin)
# admin.site.register(Record)
admin.site.site_header = '中科院公文后台管理系统'
admin.site.site_title = '中科院公文管理系统'

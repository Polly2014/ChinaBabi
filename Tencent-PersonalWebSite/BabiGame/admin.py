# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

@admin.register(BabiTrainee)
class BabiTraineeAdmin(admin.ModelAdmin):
	list_display = ('id', 'babi_id', 'babi_train_count', 'babi_role', 'babi_flag',)

@admin.register(BabiCompany)
class BabiCompanyAdmin(admin.ModelAdmin):
	list_display = ('id', 'company_address', 'company_babi', 'company_flag',)
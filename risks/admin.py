# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
#from reversion.admin import VersionAdmin
# Register your models here.

from models import *

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
	list_display = ('name',)

@admin.register(Risk)
class RiskAdmin(admin.ModelAdmin):
	list_display = ('name',)

@admin.register(RiskTypeEntity)
class RiskTypeEntityAdmin(admin.ModelAdmin):
	list_display = ('name',)

@admin.register(RiskTypeAttribute)
class RiskTypeAttributeAdmin(admin.ModelAdmin):
	list_display = ('name',)


@admin.register(RiskTypeAttributeValue)
class RiskTypeAttributeValueAdmin(admin.ModelAdmin):
	list_display = ('risk',)

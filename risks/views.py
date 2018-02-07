# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import RiskTypeEntity
from api.serializers import RiskTypeEntitySerializer
from rest_framework.renderers import JSONRenderer
# Create your views here.


def index(request):
	risk_types = RiskTypeEntity.objects.all().values('id','name')
	return render(request, 'users-list/index.html',
		context={'data':risk_types})
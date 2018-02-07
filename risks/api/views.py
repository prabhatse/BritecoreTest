#from django.views.decorators.csrf import csrf_exempt
#from rest_framework.decorators import api_view, authentication_classes, permission_classes
#from rest_framework.authentication import TokenAuthentication

from rest_framework import status, permissions
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from ..models import *
from serializers import *


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('-created_at')
    serializer_class = CompanySerializer

class RiskViewSet(viewsets.ModelViewSet):
    #permission_classes = (permissions.IsAdminUser,)
    queryset = Risk.objects.all().order_by('-created_at')
    serializer_class = RiskSerializer

class RiskTypeEntityViewSet(viewsets.ModelViewSet):
    #permission_classes = (permissions.IsAdminUser,)
    queryset = RiskTypeEntity.objects.all().order_by('-created_at')
    serializer_class = RiskTypeEntitySerializer

class RiskTypeAttributeViewSet(viewsets.ModelViewSet):
    #permission_classes = (permissions.IsAdminUser,)
    queryset = RiskTypeAttribute.objects.all().order_by('-created_at')
    serializer_class = RiskTypeAttributeSerializer

class RiskTypeAttributeValueViewSet(viewsets.ModelViewSet):
    #permission_classes = (permissions.IsAdminUser,)
    queryset = RiskTypeAttributeValue.objects.all().order_by('-created_at')
    serializer_class = RiskTypeAttributeValueSerializer

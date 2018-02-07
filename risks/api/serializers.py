from rest_framework import serializers

from ..models import *
from drf_dynamic_fields import DynamicFieldsMixin


class CompanySerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model   = Company
        fields  = ['id', 'name']

class RiskSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    company_id     = serializers.ReadOnlyField(source = 'insur_company.id')
    risk_type_name = serializers.ReadOnlyField(source = 'risk_type.name')
    

    class Meta:
        model   = Risk
        fields  = ['id', 'name', 'company_id', 'risk_type_name', 'attributes']

class RiskTypeAttributeSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    risk_id        = serializers.ReadOnlyField(source='risk.id')
    #attr_type      = serializers.SerializerMethodField()
    choices        = serializers.SerializerMethodField()

    class Meta:
        model   = RiskTypeAttribute
        fields  = ['id', 'display', 'name', 'risk_id', 'attribute_type', \
                    'default_value', 'is_required', 'choices',
                ]
    def get_attribute_type(self, obj):
        return obj.get_attribute_type_display()
    
    def get_choices(self, obj):
        choices = obj.field_choices.split(',')
        if obj.attribute_type == 's' and len(choices):
            keywords = []
            for choice in choices:
                keywords.append(choice.encode('utf-8').strip())

            return keywords
        return []


class RiskTypeEntitySerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    company_id     = serializers.ReadOnlyField(source='company.id')
    attributes     = RiskTypeAttributeSerializer(source='risk_attribute', many=True)

    class Meta:
        model   = RiskTypeEntity
        fields  = ['id', 'name', 'company_id', 'attributes',]

    
class RiskTypeAttributeValueSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    attribute_id    = serializers.ReadOnlyField(source='attribute.id')
    attribute_label = serializers.ReadOnlyField(source='attribute.display')
    risk_id         = serializers.ReadOnlyField(source='risk.id')
    
    
    class Meta:
        model   = RiskTypeAttributeValue
        fields  = ['id', 'attribute_id', 'attribute_label', 'value', 'risk_id', 'attr_type']



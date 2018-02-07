# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django import forms


class Company(models.Model):
    name             = models.CharField(
                                verbose_name = 'Company Name', 
                                max_length = 255, 
                                unique = True, 
                                blank = False, 
                                null = False
                            )

    created_at       = models.DateTimeField( 
                                verbose_name = 'Created at', 
                                auto_now_add = True
                            )

    updated_at       = models.DateTimeField(
                                verbose_name = 'Updated at', 
                                auto_now = True
                            )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Company'




class RiskTypeEntity(models.Model):
    company          = models.ForeignKey(
                                    Company, 
                                    verbose_name = 'Company', 
                                    on_delete = models.CASCADE
                                )

    name             = models.CharField(
                                    verbose_name = 'Risk Type Name', 
                                    max_length = 255
                                )

    created_at       = models.DateTimeField( 
                                verbose_name = 'Created at', 
                                auto_now_add = True
                            )

    updated_at       = models.DateTimeField(
                                verbose_name = 'Updated at', 
                                auto_now = True
                            )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Risk Type'
        unique_together = ["company", "name"]

class RiskTypeAttribute(models.Model):
    """
    A field abstract -- it describe what the field is.
    It has relationship with risk type - each risk type has multiple fields.
    """
    TYPES = (
            ('t', 'Text'),
            ('i', 'Integer'),
            ('b', 'Boolean (Yes/No)'),
            ('s', 'Dropdown Choices'),
            ('d', 'Date'),
        )

    risk_type       = models.ForeignKey(
                            RiskTypeEntity, 
                            verbose_name = 'Risk Type', 
                            on_delete = models.CASCADE,
                            related_name = 'risk_attribute'
                        )

    name            = models.CharField(
                            verbose_name = 'Risk Attribute Name', 
                            max_length = 64
                        )

    display         = models.CharField(
                            verbose_name = 'Attribute Label', 
                            max_length = 64, 
                            blank = True, 
                            null = True
                        )

    attribute_type  = models.CharField(
                            verbose_name = 'Attribute type', 
                            max_length = 1, 
                            choices = TYPES, 
                            default = 't'
                        )

    default_value   = models.CharField(
                            verbose_name = 'attribute default value',
                            max_length   = 1024,
                            blank=True,
                            null = True
                        )

    is_required     = models.BooleanField(
                            verbose_name = 'Required', 
                            default = False
                        )

    field_choices   = models.CharField(
                            max_length = 128,
                            blank=True,
                            help_text="List the choices want to displayed, comman delimited"
                        )

    created_at       = models.DateTimeField( 
                                verbose_name = 'Created at', 
                                auto_now_add = True
                            )

    updated_at       = models.DateTimeField(
                                verbose_name = 'Updated at', 
                                auto_now = True
                            )

    def __str__(self):
        return self.name

    """
    def get_form_field(self):
        field_kwargs = {
            'initial': self.default_value,
            'required': self.is_required,
        }
        if self.field_type == "b":
            return forms.BooleanField(**field_kwargs)
        elif self.field_type == "i":
            return forms.IntegerField(**field_kwargs)
        elif self.field_type == "s":
            choices = self.field_choices.split(',')
            if self.is_required is True:
                select_choices = ()
            else:
                select_choices = (('', '---------'),)
            for choice in choices:
                select_choices = select_choices + ((choice, choice),)
            return forms.ChoiceField(
                choices=select_choices, **field_kwargs)
        elif self.field_type == "d":
            return forms.DateField(**field_kwargs)
        return forms.CharField(**field_kwargs)
    """
    class Meta:
        unique_together      = ('risk_type', 'name')
        verbose_name_plural  = 'Risk Type Attributes'

class Risk(models.Model):
    name            = models.CharField(
                                verbose_name = 'Name', 
                                max_length = 255, 
                                unique = True, 
                                blank = False, 
                                null = False
                            )

    insur_company = models.ForeignKey(
                                Company,
                                verbose_name = 'Company', 
                                on_delete = models.CASCADE 
                            )  

    
    risk_type       = models.ForeignKey(
                                RiskTypeEntity,
                                verbose_name = 'Risk Type', 
                                on_delete = models.CASCADE 
                            )

    created_at       = models.DateTimeField( 
                                verbose_name = 'Created at', 
                                auto_now_add = True
                            )

    updated_at       = models.DateTimeField(
                                verbose_name = 'Updated at', 
                                auto_now = True
                            )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Risk'
    



class RiskTypeAttributeValue(models.Model):

    attribute       = models.ForeignKey(
                            RiskTypeAttribute, 
                            verbose_name = 'Risk Attribute', 
                            blank = True, 
                            null = True, 
                            related_name = 'attribute_value'
                        )

    risk            = models.ForeignKey(
                            Risk, 
                            verbose_name = 'Risk', 
                            on_delete = models.CASCADE
                        )


    value           = models.CharField(
    						verbose_name = 'Attribute value',
    						max_length = 1024,
    						blank = True,
    						null = True
						)


    created_at       = models.DateTimeField( 
                                verbose_name = 'Created at', 
                                auto_now_add = True
                            )

    updated_at       = models.DateTimeField(
                                verbose_name = 'Updated at', 
                                auto_now = True
                            )




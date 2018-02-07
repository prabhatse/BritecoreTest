# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-07 16:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('risks', '0003_auto_20180203_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risktypeattribute',
            name='risk_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='risk_attribute', to='risks.RiskTypeEntity', verbose_name='Risk Type'),
        ),
    ]

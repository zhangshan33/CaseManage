# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-25 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_auto_20190925_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itc',
            name='case_execute_time',
            field=models.DateTimeField(default='2019-09-25 11:32:15', verbose_name='测试用例执行时间'),
        ),
    ]

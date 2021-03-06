# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-17 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0024_auto_20191017_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='itc',
            name='case_cookies',
            field=models.CharField(default='', max_length=256, verbose_name='cookies'),
        ),
        migrations.AddField(
            model_name='itc',
            name='case_html_report',
            field=models.FileField(default='', upload_to='', verbose_name='用例执行结果报告'),
        ),
        migrations.AlterField(
            model_name='itc',
            name='case_execute_time',
            field=models.DateTimeField(default='2019-10-17 20:18:26', verbose_name='测试用例执行时间'),
        ),
    ]

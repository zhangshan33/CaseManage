# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-15 09:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0005_auto_20191012_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='uicase',
            name='case_media_report',
            field=models.ImageField(blank=True, upload_to="ui/b'hy\\xb7\\xf2\\xbc\\x95\\xee\\x14\\xd2\\xa0\\x12\\xach|\\xe7;'.mp4"),
        ),
        migrations.AlterField(
            model_name='uicase',
            name='case_execute_time',
            field=models.DateTimeField(default='2019-10-15 09:50:09', verbose_name='测试用例执行时间'),
        ),
    ]

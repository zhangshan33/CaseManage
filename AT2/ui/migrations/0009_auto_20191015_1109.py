# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-15 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0008_auto_20191015_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uicase',
            name='case_execute_time',
            field=models.DateTimeField(default='2019-10-15 11:09:40', verbose_name='测试用例执行时间'),
        ),
        migrations.AlterField(
            model_name='uicase',
            name='case_media_report',
            field=models.ImageField(blank=True, upload_to="ui/b'\\x9c\\x92\\xab\\x12\\xe3\\xec\\x8eG\\xc8\\xf9B2\\xf9P\\xb5\\x1c'.mp4"),
        ),
    ]

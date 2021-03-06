# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-12 14:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('web', '0013_auto_20191012_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApmCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_name', models.CharField(default='UI demo', max_length=64, verbose_name='用例名称')),
                ('case_code', models.TextField(default='', verbose_name='用例代码')),
                ('case_html_report', models.TextField(default='', verbose_name='HTML格式的用例执行结果报告')),
                ('case_priority', models.IntegerField(default=1, verbose_name='测试用例优先级')),
                ('case_create_username', models.CharField(default='好心人', max_length=64, verbose_name='测试用例创建者')),
                ('case_execute_username', models.CharField(default='好心人', max_length=64, verbose_name='测试用例执行人')),
                ('case_execute_pass', models.IntegerField(choices=[(1, '待定'), (2, '已通过'), (3, '未通过')], default=1, verbose_name='测试用例执行是否通过')),
                ('case_execute_status', models.IntegerField(choices=[(1, '未执行'), (2, '已执行')], default=1, verbose_name='测试用例状态')),
                ('case_execute_time', models.DateTimeField(default='2019-10-12 14:27:35', verbose_name='测试用例执行时间')),
                ('case_vest_project', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='web.ProjectManage', verbose_name='归属项目')),
            ],
            options={
                'ordering': ['-case_execute_time'],
            },
        ),
    ]

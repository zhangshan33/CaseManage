# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-26 06:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectManage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(default='', max_length=255, verbose_name='项目名称')),
                ('project_num', models.CharField(default='', max_length=255, verbose_name='项目代号')),
                ('project_start_time', models.DateField(default='', verbose_name='项目开始时间')),
                ('project_stop_time', models.DateField(default='', verbose_name='项目结束时间')),
                ('project_detail', models.CharField(default='', max_length=2048, verbose_name='项目描述')),
                ('project_status', models.IntegerField(default=0, verbose_name='项目状态')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(default='', max_length=255, verbose_name='模型名称')),
                ('model_num', models.CharField(default='', max_length=255, verbose_name='模型代号')),
                ('project', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='web.ProjectManage', verbose_name='所属项目')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_type', models.CharField(max_length=64, verbose_name='项目类型')),
            ],
        ),
        migrations.AddField(
            model_name='projectmanage',
            name='project_type',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='web.ProjectType', verbose_name='项目类型'),
        ),
    ]

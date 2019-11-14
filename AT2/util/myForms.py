#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "张开"
# Date: 2019/8/26


from django import forms
from django.forms import widgets as wid
from web import models


class ManageModelForm(forms.ModelForm):
    """ 项目管理的modelform """
    class Meta:
        model = models.ProjectManage
        # fields = "__all__"
        exclude = ['project_status']  # 排除哪些字段
        labels = {
            "project_name": "项目名称",
            "project_num": "项目代号",
            "project_start_time": "项目开始时间",
            "project_stop_time": "项目结束时间",
            "project_type": "项目类型",
            "project_detail": "项目描述"
        }
        error_messages = {
            "project_name": {"required": "不能为空"},
            "project_num": {"required": "不能为空"}
        }
        widgets = {
            "project_name": wid.TextInput(attrs={"class": "form-control"}),
            "project_num": wid.TextInput(attrs={"class": "form-control"}),
            "project_type": wid.Select(attrs={"class": "form-control"}),
            "project_start_time": wid.TextInput(attrs={"type": "date", "class": "form-control"}),
            "project_stop_time": wid.TextInput(attrs={"type": "date", "class": "form-control"}),
            "project_detail": wid.Textarea(attrs={"class": "form-control"}),
        }


class MdModelForm(forms.ModelForm):
    """ 模块相关的modelform """
    class Meta:
        model = models.ProjectModel
        # fields = "__all__"
        exclude = ["project"]
        labels = {
            "model_name": "模型名称",
            "model_num": "模型编号",
            "project": "所属项目,该选项无需修改"
        }
        error_messages = {
            "model_name": {"required": "不能为空"},
            "model_num": {"required": "不能为空"},
        }
        widgets = {
            "model_name": wid.TextInput(attrs={"class": "form-control"}),
            "model_num": wid.TextInput(attrs={"class": "form-control"}),
            "project": wid.TextInput(attrs={"class": "form-control", "readonly": "readonly", "disable": "disable"})
        }


class CaseModelForm(forms.ModelForm):
    """ 接口测试用例表 """
    class Meta:
        model = models.Itc   # interface testing case
        fields = "__all__"
        widgets = {
            # "case_name": wid.TextInput(attrs={"class": "form-control"}),
            "case_model": wid.TextInput(attrs={"class": "form-control"}),
            "case_priority": wid.TextInput(attrs={"class": "form-control"}),
            "case_title": wid.TextInput(attrs={"class": "form-control"}),
            "case_url": wid.TextInput(attrs={"class": "form-control"}),
            "case_header": wid.TextInput(attrs={"class": "form-control"}),
            "case_parameters": wid.TextInput(attrs={"class": "form-control"}),
            "case_parameters": wid.TextInput(attrs={"class": "form-control"}),
        }






#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "张开"
# Date: 2019/9/24

from django.conf.urls import url
from ui import views
urlpatterns = [
    url('^ui_index/(?P<pk>\d+)$', views.ui_index, name='ui_index'),
    url('^ui_execute/', views.ui_execute, name='ui_execute'),
    url('^ui_add_case/(?P<pk>\d+)$', views.ui_update_case, name='ui_add_case'),  # 添加用例
    url('^ui_edit_case/(?P<pk>\d+)$', views.ui_update_case, name='ui_edit_case'),  # 编辑用例
    url('^ui_delete_case/(?P<pk>\d+)$', views.ui_delete_case, name='ui_delete_case'),  # 编辑用例
    url('^ui_download_file/', views.ui_download_file, name='ui_download_file'),  # 下载
    url('^ui_get_case_report/', views.ui_get_case_report, name='ui_get_case_report'),  # 下载
]




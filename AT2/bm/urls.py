#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "张开"
# Date: 2019/10/12

from django.conf.urls import url
from bm import views
urlpatterns = [
    url('^bm_index/', views.bm_index, name='bm_index'),

    # url('^ui_execute/', views.ui_execute, name='ui_execute'),
    # url('^ui_add_case/(?P<pk>\d+)$', views.ui_update_case, name='ui_add_case'),  # 添加用例
    # url('^ui_edit_case/(?P<pk>\d+)$', views.ui_update_case, name='ui_edit_case'),  # 编辑用例
    # url('^ui_delete_case/(?P<pk>\d+)$', views.ui_delete_case, name='ui_delete_case'),  # 编辑用例
    # url('^ui_download_file/', views.ui_download_file, name='ui_download_file'),  # 下载
]


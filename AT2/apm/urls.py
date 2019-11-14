#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "张开"
# Date: 2019/10/12

from django.conf.urls import url
from apm import views
urlpatterns = [
    url('^apm_index/(?P<pk>\d+)$', views.apm_index, name='apm_index'),
    url('^apm_add/(?P<pk>\d+)$', views.apm_update, name='apm_add'),
    url('^apm_edit/(?P<pk>\d+)$', views.apm_update, name='apm_edit'),
    url('^apm_update/(?P<pk>\d+)$', views.apm_update, name='apm_update'),
    url('^apm_execute_cmd_command/', views.apm_execute_cmd_command, name='apm_execute_cmd_command'),

]


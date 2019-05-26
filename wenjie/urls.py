#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time     :   2019/5/13 10:40
# @Author   :   robert
# @FileName :   urls.py
# @Software :   PyCharm

from django.urls import path,re_path

from wenjie.views import *

app_name = 'wenjie'
urlpatterns = [
    path('test1',test1,name='test'),
    path('create_person',create_person),
    path('change_person',change_person),
]
#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time     :   2019/5/30 7:53
# @Author   :   robert
# @FileName :   urls.py
# @Software :   PyCharm



from django.urls import path,re_path
from ajax_demo.views import *

app_name = 'ajax_demo'
urlpatterns = [
    path('index',index),
    path('ajax_add',ajax_add),
]

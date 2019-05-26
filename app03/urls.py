#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time     :   2019/5/17 10:40
# @Author   :   robert
# @FileName :   urls.py
# @Software :   PyCharm

from django.urls import path,re_path

from app03.views import *
urlpatterns = [
    path('login',login),
    path('transfer',transfer),
    path('books',books),
    path('author',author),
]
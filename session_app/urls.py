#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time     :   2019/5/29 7:25
# @Author   :   robert
# @FileName :   urls.py
# @Software :   PyCharm

from django.urls import path,re_path
from session_app.views import *

urlpatterns = [
    path('login',login),
    path('logout',logout),
    path('home',home),
    path('transfer',transfer),
    path('books',books),
    path('author',author),
    path('user_info',UserInfo.as_view()),
]
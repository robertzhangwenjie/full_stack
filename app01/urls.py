#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time     :   2019/5/13 7:45
# @Author   :   robert
# @FileName :   urls.py
# @Software :   PyCharm

from django.urls import path,re_path
from app01.tests import *
from app01.views import *
app_name = 'app01'
urlpatterns = [
    path('login', login),
    # 作者对应关系
    path('user_list', user_list,name='user'),
    path('add_user', add_user),
    path('del_user', del_user),
    path('change_user', change_user),
    # 书籍对应关系
    path('add_book', add_book),
    path('book_list', book_list,name='book'),
    path('edit_book', edit_book),
    path('del_book', del_book),
    # 出版社对应关系
    path('publisher_list', publisher_list,name='publisher'),
    # path('add_publisher',add_publisher),
    path('add_publisher', AddPublisher.as_view()),
    path('del_publisher', del_publisher),
    path('edit_publisher', edit_publisher),
    re_path(r't_test/(?P<a>[0-9]+)/(?P<c>[0-9]+)/(?P<b>[0-9]+)/',yimi,name='test'),
    path('upload_file', upload_file),
    path('index',index),
    path('t_test2',t_test2),
    path('test',test),
    re_path('yimi/(?P<a>[0-9]+)/(?P<b>[0-9]+)/(?P<c>[0-9]+)',yimi,name='yimi'),
]
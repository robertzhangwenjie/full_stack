#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time     :   2019/5/10 22:48
# @Author   :   robert
# @FileName :   filters.py
# @Software :   PyCharm

from django import template

register = template.Library()


@register.filter(name='sb')
def sb(value):
    return 'sb{}'.format(value)
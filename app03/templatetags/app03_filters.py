#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time     :   2019/5/26 9:13
# @Author   :   robert
# @FileName :   app03_filters.py
# @Software :   PyCharm

from django import template

register = template.Library()


@register.filter
def range1(n):
    return range(1,n+1)

@register.filter
def range0(n):
    return range(n)
#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time     :   2019/5/12 6:47
# @Author   :   robert
# @FileName :   app01_mytags.py
# @Software :   PyCharm

from django import template

register = template.Library()


@register.simple_tag(name='sum')
def sum(arg1,arg2,arg3):
    return f"{arg1+arg2+arg3}"


@register.inclusion_tag(filename='result.html')
def show_results(n):
    n = 1 if n< 1 else int(n)
    data = ["第{}项".format(i) for i in range(1,n+1)]
    return {"data":data}

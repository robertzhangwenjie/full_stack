#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time     :   2019/5/10 17:45
# @Author   :   robert
# @FileName :   env.py
# @Software :   PyCharm
import functools

from django.urls import reverse
from django.templatetags.static import static
from jinja2.environment import Environment
from full_stack.jinja.filters import *

class JinjaEnvironment(Environment):
    def __init__(self,**kwargs):
        super(JinjaEnvironment, self).__init__(**kwargs)
        self.filters['sb'] = sb
        self.filters['add_str'] = add_str
        self.globals.update({
            'static':static,
            'url':reverse,
        })





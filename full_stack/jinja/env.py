#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time     :   2019/5/10 17:45
# @Author   :   robert
# @FileName :   env.py
# @Software :   PyCharm
from jinja2.environment import Environment
from full_stack.jinja.filters import sb

class JinjaEnvironment(Environment):
    def __init__(self,**kwargs):
        super(JinjaEnvironment, self).__init__(**kwargs)
        self.filters['sb'] = sb


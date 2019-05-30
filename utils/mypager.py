#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time     :   2019/5/26 19:32
# @Author   :   robert
# @FileName :   mypager.py
# @Software :   PyCharm

'''
分页器
'''

import math

class Page(object):

    def __init__(self, page_num, total_count, page_size=10, max_page=11):
        '''

        :param page_num: 访问的页码
        :param total_count: 总数
        :param page_size: 每页显示的数量
        :param max_page: 最多显示多少个页码
        '''
        self.page_num = int(page_num)
        self.total_count = total_count
        self.page_size = int(page_size)
        self.max_page = int(max_page)

    def start(self):
        return (self.page_num-1)*self.page_size

    def end(self):
        return self.START + self.page_size

    # 给类设置属性START和END，分别对应当前页的显示的第一个和最后一个元素
    START = property(start)
    END = property(end)

    def page_html(self,url_prefix):
        '''

        :param url_prefix: url的前缀
        :return: 分页器的html的str
        '''
        # 获取最大页数
        pages = math.ceil(self.total_count / self.page_size)
        # 分页器的中间页数
        middle_number = math.ceil(self.max_page / 2)
        # 中间页数到第一页的数量
        page_middle = self.page_num
        # 获取第一页页码
        page_start = page_middle - middle_number+1
        # 如果第一页小于1则第一页应该是1
        if page_start <= 0:
            page_start = 1
        # 最后一页 = 第一页 + 显示的最多页 -1
        page_end = page_start + self.max_page -1

        # 如果最后一页大于系统的最大页数，则最后一页应该是系统的最大页
        if page_end >= pages:
            page_end = pages
            page_start = page_end - self.max_page + 1
            if page_start <= 0:
                page_start = 1

        # 如果访问的页码大于最后的页码，默认访问最后一页
        self.page_num = pages if self.page_num >= pages else self.page_num

        # 定义一个分页器的列表
        pager_list = []

        # 返回第一页的li标签
        first_page_html = '''<li><a href="{url}?page={0}&pageNumber={1}">首页</a></li>'''.format(1, self.page_size, url=url_prefix)
        pager_list.append(first_page_html)

        # 返回上一页的li标签
        pre_page_html = '''<li class='previous'><a href="{url}?page={0}&pageNumber={1}"><span>&laquo;</span></a></li>'''.format(
            self.page_num - 1, self.page_size,url=url_prefix)
        # 如果当前页是第一页，上一页按钮不可点击
        if self.page_num == 1:
            pre_page_html = '''<li class="previous disabled"><a href="{url}?page={0}&pageNumber={1}"><span>&laquo;</span></a></li>'''.format(
                self.page_num - 1, self.page_size,url=url_prefix)
        pager_list.append(pre_page_html)

        for i in range(page_start, page_end + 1):
            # 当页数为当前页时，增加class active
            if i == self.page_num:
                html_str = '''<li class='active'><a href="{url}?page={0}&pageNumber={1}">{0}</a></li>'''.format(i, self.page_size, url=url_prefix)
            else:
                html_str = '''
                 <li><a href="{url}?page={0}&pageNumber={1}">{0}</a></li>'''.format(i, self.page_size, url=url_prefix)
            pager_list.append(html_str)

        # 下一页
        next_page_html = '''<li class="next"><a href="{url}?page={0}&pageNumber={1}"><span>&raquo;</span></a></li>'''.format(
            self.page_num + 1, self.page_size,url=url_prefix)
        # 如果当前页为最后一页，下一页按钮不可点击
        if self.page_num >= pages:
            next_page_html = '''<li class="next disabled"><a href="{url}?page={0}&pageNumber={1}"><span>&raquo;</span></a></li>'''.format(
                self.page_num + 1, self.page_size,url=url_prefix)
        pager_list.append(next_page_html)

        # 访问最后一页的li标签
        last_page_html = '''<li><a href="{url}?page={0}&pageNumber={1}">尾页</a></li>'''.format(pages, self.page_size, url=url_prefix)
        pager_list.append(last_page_html)
        # 组成分页的html
        pager_html = ''.join(pager_list)
        return pager_html



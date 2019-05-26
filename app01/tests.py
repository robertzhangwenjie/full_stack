import datetime

from django.http import JsonResponse
from django.test import TestCase
from django.shortcuts import  render,redirect,HttpResponse
from django.urls import reverse
from app01.models import *
# Create your tests here.


# 测试类
class Person(object):
    def __init__(self):
        self.name = 1
        self.age = 22

    def get_bar(self):
        print('getter...')
        return 'laowang'

    def set_bar(self,value):
        print('setter...')
        return 'set value' + value

    def del_bar(self):
        print('deleter ...')
        return 'laowang'


def t_test(request):
    name_list = [1,2,3,4]
    name_dict = {'first_name':'wenjie','last_name':'zhang'}
    person = Person()
    file_size = 10240
    slice_str = 'robertwenjie'
    html = "<p>testfsdsfdsfdsfs<p>"
    person = 'robert'
    greeting = 'heelo'
    # return render(request, 'test.html', locals())
    return JsonResponse(name_list,safe=False)


def t_test2(request):

    return redirect(reverse('test',kwargs={'a':1,'b':2,'c':3}))


def yimi(request,a,b,c):
    ret = [a,b,c]
    return JsonResponse(ret,safe=False)

def test(request):
    return render(request,'yimi.html')


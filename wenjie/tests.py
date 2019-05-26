from django.test import TestCase

# Create your tests here.
'''
如何在一个python项目中加载整个项目的环境的变量和配置信息
'''

import os

if __name__ == '__main__':
    # 加载django项目的配置信息
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'full_stack.settings')
    # 导入django，并启动django项目
    import django
    django.setup()

    # from app01 import models
    from wenjie import models


    from django.db.models.functions import Concat
    from django.db.models import Value
    from django.db.models import F,Q

    # 一对一修改
    # ret = models.Author.objects.get(id=2)
    ret = models.AuthorDetail.objects.get(id=2)
    ret.phone = 888888
    ret.save()



    # ret = models.Author.objects.create(name='wenjie')
    # ret.detail = models.AuthorDetail.objects.create(hobby='123',phone=12345,addr='222')
    # ret.save()


    # 查询价格小于100或者库存大于2000的所有书,且id小于4
    # ret = models.Book.objects.filter(Q(price__lt=100) | Q(inventory__gt=2000),id__lt=4)
    # print(ret)
    #
    # from django.db import transaction
    #
    # with transaction.atomic():
    #     pass
    #
    # ret = models.Book.objects.filter(price__gt=9)
    # print(ret)

    # 查询库存数大于卖出数的所有书
    # ret = models.Book.objects.all().values_list('inventory','quantity_sold')
    # for i in ret:
    #    if i[0] > i[1]:
    #        print(i)

    # from django.db.models import F
    # # 两个字段作比较时用F,F用来取出值，可以进行算数运算
    # ret = models.Book.objects.all().filter(inventory__gt=F('quantity_sold'))
    # print(ret)
    # # 给卖出数量*3倍
    # models.Book.objects.all().update(quantity_sold=F('quantity_sold')*3)
    # models.Book.objects.all().update(quantity_sold=(F('quantity_sold')+30)+2)
    #

    # 聚合查询
    from django.db.models import Avg,Sum,Max,Min,Count
    # avg_test = models.Book.objects.all().aggregate(avg = Avg('price')) # 默认返回的dict中，key为price__avg,通过设置key = 来自定义
    # sum_test = models.Book.objects.all().aggregate(Sum('price'))
    # max_test = models.Book.objects.all().aggregate(Max('price'))
    # min_test = models.Book.objects.all().aggregate(Min('price'))
    # # 多个条件查询
    # avg_sum = models.Book.objects.all().aggregate(avg=Avg('price'),sum=Sum('price'))
    # print(avg_sum['sum'])
    # models.Author.objects.filter(id=1).first().book.add(1)
    # 分组查询
    # 查询每一本书的作者个数
    # book_list = models.Book.objects.all().annotate(author_num=Count('author'))

    # book_list = models.Book.objects.all().annotate(author_num=Count('author')).filter(author_num__gt=0)
    # print(book_list)
    # for book in book_list:
    #     print(book.author_num)
    #
    # # 查出Author的一个对象
    # # author_first = models.Author.objects.filter(id=1).first()
    # # 查出该对象的关系管理对象ret.book也就是关联的所有的book对象管理器
    # # 在调用关系管理对象的all方法查询所有的book对象
    #
    # # ret = author_first.book.create(title='我', publisher_id=2)
    # # # print(ret)
    # # # ret = models.Book(title='们',publisher_id=3)
    # # # ret.save()
    # # # 添加对象
    # # # book_obj = models.Book.objects.filter(id__gt=2).first()
    # # # print(book_obj)
    # # # author_first.book.add(book_obj)
    # # # # # 添加多个对象
    # # book_objs = models.Book.objects.filter(id__gt=3)
    # # author_first.book.add(*book_objs)
    # # # 添加id
    # # # author_first.book.add(3)
    # # # 添加多个id
    # # # author_first.book.add(*[1,2,3])
    # #
    # #
    # # # # 更新关联的对象，相当于重新关联
    # # # author_first.book.set([6, 7])
    # # #
    # # # # 删除关联的对象--根据id
    # # author_first.book.remove(6)
    # # # 删除多个对象--根据id
    # # author_first.book.remove(*[6,7,8])
    # # #
    # # # # 删除关联的对象--根据对象
    # # remove_obj = models.Book.objects.filter(id__gt=7)
    # # author_first.book.remove(remove_obj)
    # # # 删除多个对象--根据对象
    # # author_first.book.remove(*remove_obj)
    #
    #
    # # 清空
    # # author_first.book.clear()
    # # 先查询出id=2的QuerySet对象
    # # ret = models.Publisher.objects.filter(id=2)
    # # # 根据字段名查询QuerySet的所有的values对象
    # # # 反向查询时，写book_set__title跨表查询，或者使用定义的related_name-books代替book_set
    # # ret = ret.values('books__title')
    # # print(ret)
    # ret = models.Author.objects.all().annotate(price_sum=Sum('book__price')).values('name','price_sum')
    # print(ret)
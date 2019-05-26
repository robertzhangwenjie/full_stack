import datetime

import django
from django.db import models

# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=30,null=False)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=18)
    birthday = models.DateField(default=datetime.datetime(year=1990,month=8,day=9))
    create_time = models.DateTimeField(auto_now_add=True)
    change_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# 作者
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False,max_length=20)
    detail = models.OneToOneField(to='AuthorDetail',on_delete=models.CASCADE)

    def __str__(self):
        return "<{}-{}>".format(self.id,self.name)

# 作者详情
class AuthorDetail(models.Model):
    id = models.AutoField(primary_key=True)
    hobby = models.CharField(max_length=32)
    phone = models.IntegerField()
    addr = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.id}=={self.addr}'






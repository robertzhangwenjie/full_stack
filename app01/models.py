from django.db import models

# Create your models here.

# 作者
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False,max_length=20)
    book = models.ManyToManyField(to='Book')
    detail = models.OneToOneField(to='AuthorDetail',on_delete=models.CASCADE,default=None,null=True)
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


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64,null=False)
    price = models.DecimalField(max_digits=6,decimal_places=2,null=True,default=99.99)
    inventory = models.IntegerField(default=9999)
    quantity_sold = models.PositiveIntegerField(default=0)
    publisher = models.ForeignKey(to="Publisher",on_delete=models.SET_NULL,blank=True,null=True,default=1,related_name='books')

    def __str__(self):
        return "<{}-{}-{}>".format(self.id,self.title,self.publisher)

class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40,null=False,unique=True)
    addr = models.CharField(max_length=200,null=True,default=None)

    def __str__(self):
        return "<{}-{}>".format(self.name,self.addr)


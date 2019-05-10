from django.db import models

# Create your models here.

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False,max_length=20)
    book = models.ManyToManyField(to='Book')
    def __str__(self):
        return "<{}-{}>".format(self.id,self.name)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64,null=False)
    publisher = models.ForeignKey(to="Publisher",on_delete=models.SET_NULL,blank=True,null=True,default=1)

    def __str__(self):
        return "<{}-{}-{}>".format(self.id,self.title,self.publisher)





class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40,null=False,unique=True)
    addr = models.CharField(max_length=200,null=True,default=None)

    def __str__(self):
        return "<{}-{}>".format(self.name,self.addr)
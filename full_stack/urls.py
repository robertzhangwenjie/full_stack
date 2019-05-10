"""full_stack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from app01.views import *
from app01.tests import *

urlpatterns = [
    path('',index),
    path('admin/', admin.site.urls),
    path('login',login),
    # 作者对应关系
    path('user_list',user_list),
    path('add_user',add_user),
    path('del_user',del_user),
    path('change_user',change_user),
    # 书籍对应关系
    path('add_book',add_book),
    path('book_list',book_list),
    path('edit_book',edit_book),
    path('del_book',del_book),
    # 出版社对应关系
    path('publisher_list',publisher_list),
    path('add_publisher',add_publisher),
    path('del_publisher',del_publisher),
    path('edit_publisher',edit_publisher),
    # 测试
    path('t_test',t_test),
]

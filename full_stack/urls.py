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
from django.urls import path,re_path,include
from app01.views import *
import app01.urls
import app03.urls
import session_app.urls
import wenjie.urls
import ajax_demo.urls

urlpatterns = [
    re_path(r'^wenjie/',include(wenjie.urls)),
    path('admin/', admin.site.urls),
    re_path(r'^app01/',include(app01.urls)),
    re_path(r'^app03/',include(app03.urls)),
    re_path(r'^session_app/',include(session_app.urls)),
    re_path(r'^ajax_demo/',include(ajax_demo.urls)),
]

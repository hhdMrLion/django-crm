"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include

from users import views

urlpatterns = [
    # admin后台页面
    path('admin/', admin.site.urls),
    # index重定向
    path('', views.index, name='index'),
    # home首页
    path('home/', views.home, name='home'),
    # week周数据汇总
    path('week/', views.week, name='week'),
    # path('week/group', views.week_group, name='week_group'),
    path('week/all', views.week_all, name='week_all'),
    # 用户模块
    path('user/', include('users.urls')),
    # 客户信息模块
    path('customer/', include('customer.urls')),
    # 联系人信息模块
    path('liaison/', include('liaison.urls')),
    # 拜访记录模块
    path('record/', include('record.urls')),
    # 商机模块
    path('business/', include('business.urls')),
    # okr模块
    path('okr/', include('okr.urls'))
]

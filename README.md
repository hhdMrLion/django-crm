# django-crm
* 该为上一个DJANGO_CRM的重构项目，升级到django2.2，添加权限关系，优化添加查看筛选的功能，考虑未来做成前后分离的项目，先重构到2.0，再慢慢升级成vue+djangorestframework的前后端分离的项目

### 11.25更新
* 今天起开始进行项目的重构，为客户关系系统解决方案提供另外一种思路
* 在原先功能的基础上，引入权限管理，用不同角色来对应不同的操作

### 12.21更新
* 完成用户模块和权限分配

### 12.25更新
* 完成客户模块
* 完成联系人模块
* 完成客户拜访记录模块

### 12.28更新
* 完成所有的基本功能
* 未完成的地方：首页统计，权限赋值，商机产品
* 完成首页的数据统计功能

### 12.29更新
* 目前找到一个小bug，在首页进行数据统计时，每个用户只有在登录的时候才能更新自己的数据，这样，如果一个用户很久没登陆，那么他是数据
就没法进行实时更新，这样在经理看到的时候都是假数据，所以要做一个能实时更新首页数据的功能，也就是重置数据为零。
* 现一个解决方案，访问首页的时候不去对单个用户进行渲染，直接一次性获取所有用户信息，批量进行渲染。

* ~~目前还有一个问题有待解决，在添加完客户添加联系人等其它信息时，在前端页面上选择客户会读取到所有的客户信息，这里应该只返回该用户下面的客户，而不是所有客户。~~

* 增加经理的功能，让其可以查看所有人的业务信息

### 12.31更新
* 解决同域名下多个项目session冲突问题

### 1.7更新
* 完善客户详情页
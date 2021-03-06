from django.urls import path

from record import views
from record.views import RecordView

urlpatterns = [
    # 查看拜访记录
    path('', RecordView.as_view(), name='record'),
    # 添加拜访记录
    path('add/', views.record_add, name='record_add'),
    # 查看和修改拜访记录
    path('detail/<int:pk>', views.record_detail, name='record_detail'),
    # 单个页面进行修改
    path('edit/<int:pk>', views.record_edit, name='record_edit'),
    # 删除拜访记录
    path('delete/<int:pk>', views.record_delete, name='record_delete'),

    # 团队拜访记录
    path('group/', views.record_group, name='record_group'),

    # 所有拜访记录列表
    path('all/', views.record_all, name='record_all'),
    # 客户详情
    path('all/detail/<int:pk>', views.record_all_detail, name='record_all_detail'),

    # 导出所有拜访记录信息
    path('export/record', views.export_record, name='export_record'),
]
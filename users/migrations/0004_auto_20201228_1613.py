# Generated by Django 2.2.17 on 2020-12-28 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201228_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='Count',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='用户id')),
                ('name', models.CharField(blank=True, max_length=64, null=True, verbose_name='姓名')),
                ('day_customer', models.IntegerField(default=0, verbose_name='今天新增客户数量')),
                ('day_liaison', models.IntegerField(default=0, verbose_name='今天新增联系人数量')),
                ('day_record', models.IntegerField(default=0, verbose_name='今天新增拜访记录数量')),
                ('day_business', models.IntegerField(default=0, verbose_name='今天新增商机数量')),
                ('mouth_customer', models.IntegerField(default=0, verbose_name='本月新增客户数量')),
                ('mouth_liaison', models.IntegerField(default=0, verbose_name='本月新增联系人数量')),
                ('mouth_record', models.IntegerField(default=0, verbose_name='本月新增拜访记录数量')),
                ('mouth_business', models.IntegerField(default=0, verbose_name='本月新增商机数量')),
                ('all_customer', models.IntegerField(default=0, verbose_name='全部客户数量')),
                ('all_liaison', models.IntegerField(default=0, verbose_name='全部联系人数量')),
                ('all_record', models.IntegerField(default=0, verbose_name='全部拜访记录数量')),
                ('all_business', models.IntegerField(default=0, verbose_name='全部商机数量')),
            ],
            options={
                'verbose_name': '用户数据统计',
                'verbose_name_plural': '用户数据统计',
                'db_table': 'count',
            },
        ),
        migrations.DeleteModel(
            name='UserCount',
        ),
    ]

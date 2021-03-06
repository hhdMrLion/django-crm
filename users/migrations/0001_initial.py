# Generated by Django 2.2.17 on 2020-12-21 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=256, verbose_name='密码')),
                ('is_valid', models.BooleanField(default=True, verbose_name='是否有效')),
                ('professional', models.CharField(blank=True, max_length=64, null=True, verbose_name='职称')),
                ('role', models.SmallIntegerField(choices=[(1, '业务'), (2, '主管'), (3, '商务'), (4, '经理'), (5, '人事')], default=1, verbose_name='权限')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'users',
                'ordering': ['-created_time'],
            },
        ),
    ]

# Generated by Django 2.2.17 on 2021-03-15 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210310_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='count',
            name='all_customer',
        ),
        migrations.AddField(
            model_name='count',
            name='month_customer',
            field=models.IntegerField(default=0, verbose_name='本月客户数量'),
        ),
    ]

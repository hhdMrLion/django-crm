# Generated by Django 2.2.17 on 2020-12-28 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0003_record_theme'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='record',
            options={'ordering': ['-created_at'], 'verbose_name': '客户拜访记录', 'verbose_name_plural': '客户拜访记录'},
        ),
    ]

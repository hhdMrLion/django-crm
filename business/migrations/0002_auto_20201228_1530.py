# Generated by Django 2.2.17 on 2020-12-28 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='business',
            options={'ordering': ['-created_at'], 'verbose_name': '客户商机', 'verbose_name_plural': '客户商机'},
        ),
    ]

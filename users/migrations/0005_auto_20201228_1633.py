# Generated by Django 2.2.17 on 2020-12-28 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201228_1613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='count',
            old_name='mouth_business',
            new_name='month_business',
        ),
        migrations.RenameField(
            model_name='count',
            old_name='mouth_customer',
            new_name='month_customer',
        ),
        migrations.RenameField(
            model_name='count',
            old_name='mouth_liaison',
            new_name='month_liaison',
        ),
        migrations.RenameField(
            model_name='count',
            old_name='mouth_record',
            new_name='month_record',
        ),
    ]

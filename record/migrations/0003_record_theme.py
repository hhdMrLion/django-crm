# Generated by Django 2.2.17 on 2020-12-28 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_auto_20201225_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='theme',
            field=models.CharField(default=1980, max_length=256, verbose_name='拜访主题'),
            preserve_default=False,
        ),
    ]

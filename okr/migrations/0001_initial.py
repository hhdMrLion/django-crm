# Generated by Django 2.2.17 on 2021-03-29 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0010_user_up_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Okr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object', models.CharField(max_length=255, verbose_name='目标')),
                ('key1', models.CharField(blank=True, max_length=255, null=True, verbose_name='关键成果1')),
                ('key1_true', models.BooleanField(blank=True, default=False, null=True, verbose_name='完成情况1')),
                ('key2', models.CharField(blank=True, max_length=255, null=True, verbose_name='关键成果2')),
                ('key2_true', models.BooleanField(blank=True, default=False, null=True, verbose_name='完成情况2')),
                ('key3', models.CharField(blank=True, max_length=255, null=True, verbose_name='关键成果3')),
                ('key3_true', models.BooleanField(blank=True, default=False, null=True, verbose_name='完成情况3')),
                ('results', models.CharField(blank=True, max_length=255, null=True, verbose_name='衡量标准')),
                ('finish', models.CharField(blank=True, max_length=255, null=True, verbose_name='实际达成')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_valid', models.BooleanField(default=True, verbose_name='是否有效')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User', verbose_name='创建人')),
            ],
            options={
                'verbose_name': 'okr',
                'verbose_name_plural': 'okr',
                'db_table': 'okr',
                'ordering': ['-created_at'],
            },
        ),
    ]

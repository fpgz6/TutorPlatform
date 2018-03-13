# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-13 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20180310_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_type',
            field=models.IntegerField(choices=[(0, '没有注册'), (1, '教师'), (2, '学生')], default=0, help_text='0: 没有注册 1: 教师 2: 学生', verbose_name='用户角色'),
        ),
    ]
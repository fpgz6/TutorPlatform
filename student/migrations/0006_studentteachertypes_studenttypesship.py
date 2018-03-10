# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-10 15:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20180310_1537'),
        ('student', '0005_auto_20180308_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentTeacherTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student', verbose_name='学生')),
                ('teacher_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.TeacherType', verbose_name='教学特点')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentTypesShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student', verbose_name='学生')),
                ('student_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.StudentType', verbose_name='存在问题')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

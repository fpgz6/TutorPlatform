# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-26 10:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import libs.uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0003_school'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('uid', models.CharField(default=libs.uuid.create_teacher_uid, max_length=16, unique=True, verbose_name='\u6559\u5e08ID')),
                ('last_name', models.CharField(max_length=4, verbose_name='\u59d3\u6c0f')),
                ('phone', models.CharField(max_length=16, verbose_name='\u7535\u8bdd')),
                ('sex', models.IntegerField(default=0, help_text='0\uff1a\u5973 1\uff1a\u7537', verbose_name='\u6027\u522b')),
                ('learn', models.IntegerField(choices=[(0, '\u6682\u65e0'), (1, b'\xe6\x9c\xac\xe7\xa7\x91'), (2, b'\xe7\xa0\x94\xe7\xa9\xb6\xe7\x94\x9f')], default=0, verbose_name='\u5b66\u5386')),
                ('profession', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u4e13\u4e1a')),
                ('money', models.IntegerField(default=0, help_text='\u9ed8\u8ba4\u5355\u4f4d\uff1a\u5c0f\u65f6', verbose_name='\u671f\u671b\u85aa\u8d44')),
                ('is_valid', models.BooleanField(default=True, verbose_name='\u662f\u5426\u6709\u6548')),
                ('head_image', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u5934\u50cf')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.City', verbose_name='\u57ce\u5e02')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.Customer', verbose_name='\u7528\u6237')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.School', verbose_name='\u5b66\u6821')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TeacherSubjectsShip',
            fields=[
                ('subject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.Subject')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_subject', to='common.Subject', verbose_name='\u5b66\u79d1')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Teacher', verbose_name='\u6559\u5e08')),
            ],
            options={
                'abstract': False,
            },
            bases=('common.subject',),
        ),
    ]

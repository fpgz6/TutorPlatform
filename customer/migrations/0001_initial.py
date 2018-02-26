# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-26 10:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.CharField(max_length=64, unique=True, verbose_name='\u5fae\u4fe1ID')),
                ('nickname', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u5fae\u4fe1\u540d\u79f0')),
                ('avatar_url', models.URLField(blank=True, help_text='\u5934\u50cf', null=True, verbose_name='\u5934\u50cf')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

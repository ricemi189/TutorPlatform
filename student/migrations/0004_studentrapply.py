# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-18 21:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('student', '0003_student_baselevel'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentrApply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('apply_type', models.IntegerField(default=1, help_text='1：老师 2：学生', verbose_name='申请者类型, 目前教师仅能被学生申请')),
                ('is_valid', models.BooleanField(default=True, verbose_name='是否有效')),
                ('customer', models.ForeignKey(help_text='申请者', null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
                ('student', models.ForeignKey(help_text='学生', on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
            options={
                'verbose_name': '老师被申请列表',
                'verbose_name_plural': '老师被申请列表',
            },
        ),
    ]

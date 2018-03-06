# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-26 08:41
from __future__ import unicode_literals

from django.db import migrations, models
import libs.uuid


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='uid',
            field=models.CharField(default=libs.uuid.create_student_uid, max_length=16, unique=True, verbose_name='\u5b66\u751fID'),
        ),
    ]
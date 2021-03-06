# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-22 16:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_reason'),
        ('customer', '0007_suggestionimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuggestionReason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('reason', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Reason', verbose_name='投诉原因')),
                ('suggestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.CustomerSuggestion', verbose_name='投诉表')),
            ],
            options={
                'verbose_name': '投诉原因',
                'verbose_name_plural': '投诉原因',
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-20 10:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import libs.uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_customer_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerTokenShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('token', models.CharField(default=libs.uuid.create_uuid, max_length=36, verbose_name='TOKEN')),
                ('expire_time', models.IntegerField(default=0, verbose_name='超时时间')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.DeleteModel(
            name='WXUser',
        ),
        migrations.AddField(
            model_name='customertokenship',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer', verbose_name='用户'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10b1 on 2016-09-04 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childrens_desktop', '0004_auto_20160824_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desktopuser',
            name='username',
            field=models.CharField(error_messages={b'unique': b'this username already exist'}, max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='desktopusermanager',
            name='email',
            field=models.CharField(default=b'', max_length=60, unique=True),
        ),
    ]

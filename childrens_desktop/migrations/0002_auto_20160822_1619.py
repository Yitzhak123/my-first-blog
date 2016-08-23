# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-22 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childrens_desktop', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DesktopUserManagerLoginDetails',
        ),
        migrations.RemoveField(
            model_name='desktopusermanager',
            name='desktop_users',
        ),
        migrations.AddField(
            model_name='desktopuser',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='desktopusermanager',
            name='desktop_users_group',
            field=models.TextField(default='[]'),
        ),
    ]
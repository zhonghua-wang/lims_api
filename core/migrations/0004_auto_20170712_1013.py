# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 02:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170712_1012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='birth_data',
            new_name='birth_date',
        ),
    ]
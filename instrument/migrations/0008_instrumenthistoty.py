# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-10 16:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instrument', '0007_auto_20170810_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstrumentHistoty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instrument.Instrument')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

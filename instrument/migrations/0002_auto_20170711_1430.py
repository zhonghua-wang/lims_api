# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 06:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChargeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='instrument',
            name='accessories',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='application',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='reservation_end_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='reservation_start_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='reservation_time_unit',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='instrument',
            name='charge_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='instrument.ChargeType'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
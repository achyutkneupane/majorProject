# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-29 20:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20191030_0140'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ['roll']},
        ),
    ]
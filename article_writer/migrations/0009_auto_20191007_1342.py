# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-07 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_writer', '0008_auto_20191007_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='star3.jpeg', upload_to=b''),
        ),
    ]

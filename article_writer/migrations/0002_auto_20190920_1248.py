# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-20 12:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article_writer', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Article',
            new_name='Articles',
        ),
    ]
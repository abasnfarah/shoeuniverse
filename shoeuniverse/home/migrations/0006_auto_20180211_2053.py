# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-11 20:53
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20180113_1746'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoehistorypage',
            old_name='shoeImage',
            new_name='banner',
        ),
        migrations.AlterField(
            model_name='newcontributer',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributers', to='home.AboutPage'),
        ),
    ]

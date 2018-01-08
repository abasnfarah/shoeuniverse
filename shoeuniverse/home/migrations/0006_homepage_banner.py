# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-08 04:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('home', '0005_homeshoetile_shoehistorypage_styleshoetile'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]

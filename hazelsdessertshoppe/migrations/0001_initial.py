# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import hazelsdessertshoppe.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('category', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('price', models.FloatField(max_length=300)),
                ('category', models.ForeignKey(to='hazelsdessertshoppe.Category', on_delete=models.SET(hazelsdessertshoppe.models.get_default_category))),
            ],
        ),
    ]

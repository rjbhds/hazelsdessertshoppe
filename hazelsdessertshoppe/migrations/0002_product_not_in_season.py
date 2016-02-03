# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hazelsdessertshoppe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='not_in_season',
            field=models.BooleanField(default=False),
        ),
    ]

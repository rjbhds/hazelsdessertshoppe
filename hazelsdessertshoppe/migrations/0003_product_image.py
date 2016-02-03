# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import hazelsdessertshoppe.models


class Migration(migrations.Migration):

    dependencies = [
        ('hazelsdessertshoppe', '0002_product_not_in_season'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=hazelsdessertshoppe.models.get_image_file_path, null=True, blank=True),
        ),
    ]

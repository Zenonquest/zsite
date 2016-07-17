# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gmaps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinates',
            name='latitude',
            field=models.FloatField(max_length=200),
        ),
        migrations.AlterField(
            model_name='coordinates',
            name='longitude',
            field=models.FloatField(max_length=200),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0005_auto_20151122_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='site_vote',
            field=models.IntegerField(default=0),
        ),
    ]

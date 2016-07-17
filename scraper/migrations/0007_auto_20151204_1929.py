# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0006_site_site_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='site_vote',
            field=models.IntegerField(default=2),
        ),
    ]

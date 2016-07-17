# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0004_remove_sitelink_link_html'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitelink',
            name='link_html',
            field=models.TextField(default=datetime.datetime(2015, 11, 22, 22, 4, 23, 985000, tzinfo=utc), max_length=20000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sitelink',
            name='link_content',
            field=models.TextField(max_length=200000),
        ),
    ]

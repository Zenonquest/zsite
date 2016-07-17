# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0002_auto_20151115_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 15, 22, 55, 44, 644000, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitelink',
            name='link_html',
            field=models.CharField(default=' ', max_length=2000),
            preserve_default=False,
        ),
    ]

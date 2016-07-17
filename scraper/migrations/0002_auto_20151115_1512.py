# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitelink',
            name='link_content',
            field=models.CharField(max_length=200000),
        ),
        migrations.AlterField(
            model_name='sitelink',
            name='link_text',
            field=models.CharField(max_length=2000),
        ),
    ]

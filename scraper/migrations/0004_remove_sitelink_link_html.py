# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0003_auto_20151115_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitelink',
            name='link_html',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SiteLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link_text', models.CharField(max_length=200)),
                ('link_content', models.CharField(max_length=200)),
                ('site', models.ForeignKey(to='scraper.Site')),
            ],
        ),
    ]

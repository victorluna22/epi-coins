# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_auto_20150909_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='value',
        ),
    ]

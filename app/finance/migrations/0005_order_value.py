# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_remove_order_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='value',
            field=models.DecimalField(default=0, verbose_name='Valor', max_digits=10, decimal_places=2),
        ),
    ]

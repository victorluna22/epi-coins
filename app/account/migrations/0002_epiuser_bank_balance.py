# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='epiuser',
            name='bank_balance',
            field=models.DecimalField(default=0, verbose_name=b'Saldo', max_digits=10, decimal_places=2),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name': 'transa\xe7\xe3o', 'verbose_name_plural': 'transa\xe7\xf5es'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'pedido', 'verbose_name_plural': 'pedidos'},
        ),
        migrations.AddField(
            model_name='activity',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 2, 43, 16, 79404, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]

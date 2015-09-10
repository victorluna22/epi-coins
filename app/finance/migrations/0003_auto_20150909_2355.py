# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20150909_2343'),
        ('finance', '0002_auto_20150909_2343'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qtd', models.IntegerField(verbose_name='Quantidade')),
            ],
            options={
                'verbose_name': 'item',
                'verbose_name_plural': 'itens',
            },
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'compra', 'verbose_name_plural': 'compras'},
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(related_name='items', to='finance.Order'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(to='product.Product'),
        ),
    ]

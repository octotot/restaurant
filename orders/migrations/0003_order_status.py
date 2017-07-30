# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20170731_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Принят'), (1, 'Оплачен'), (2, 'Исполнен'), (3, 'Отменен')], default=0, verbose_name='Статус'),
            preserve_default=False,
        ),
    ]

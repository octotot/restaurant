# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 09:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dish',
            options={'verbose_name': 'Блюдо', 'verbose_name_plural': 'Блюда'},
        ),
        migrations.AlterModelOptions(
            name='dishcategory',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='restaurant',
            options={'verbose_name': 'Ресторан', 'verbose_name_plural': 'Рестораны'},
        ),
        migrations.AddField(
            model_name='orderitem',
            name='count',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название блюда'),
        ),
        migrations.AlterField(
            model_name='dishcategory',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='dishcategory',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='orders.DishCategory'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.Order'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.PositiveIntegerField(editable=False, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='city',
            field=models.CharField(choices=[('MSK', 'Москва'), ('SPB', 'Санкт-Петербург')], max_length=3, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название ресторана'),
        ),
        migrations.AlterUniqueTogether(
            name='dishcategory',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='dishcategory',
            name='slug',
        ),
    ]

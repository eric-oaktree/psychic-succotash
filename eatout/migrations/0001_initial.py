# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-04 21:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dinner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date', models.DateField()),
                ('attendance', models.IntegerField(default=1)),
                ('spent', models.DecimalField(decimal_places=2, max_digits=19)),
                ('e_mood', models.CharField(blank=True, max_length=3, null=True)),
                ('t_mood', models.CharField(blank=True, max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('genre', models.TextField()),
                ('address', models.TextField(blank=True, null=True)),
                ('lat', models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True)),
                ('lon', models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='dinner',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eatout.Restaurant'),
        ),
    ]
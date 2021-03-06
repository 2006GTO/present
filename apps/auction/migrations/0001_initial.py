# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-27 23:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('years', models.IntegerField(max_length=1)),
                ('salary', models.IntegerField(max_length=3)),
                ('position', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=32)),
                ('team_name', models.CharField(max_length=32)),
                ('slogan', models.TextField(max_length=160)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='has_manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='has_player', to='auction.User'),
        ),
        migrations.AddField(
            model_name='player',
            name='on_roster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='has_roster', to='auction.User'),
        ),
    ]

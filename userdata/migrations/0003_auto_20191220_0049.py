# Generated by Django 2.2.5 on 2019-12-19 19:19

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0002_auto_20191219_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='roles',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=None),
        ),
    ]

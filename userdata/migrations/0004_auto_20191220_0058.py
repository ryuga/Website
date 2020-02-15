# Generated by Django 2.2.5 on 2019-12-19 19:28

import django.contrib.postgres.fields
from django.db import migrations, models
import userdata.models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0003_auto_20191220_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='roles',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=userdata.models.default_array, null=True, size=None),
        ),
    ]

# Generated by Django 2.2.5 on 2020-03-26 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('websitedata', '0010_privacy_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='privacy',
            name='number',
        ),
    ]
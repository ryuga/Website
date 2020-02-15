# Generated by Django 2.2.5 on 2019-12-08 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websitedata', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='color',
        ),
        migrations.AddField(
            model_name='projects',
            name='brief',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='projects',
            name='label',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='projects',
            name='status',
            field=models.CharField(choices=[('score yellow', 'Completed'), ('score purple', 'Refactoring'), ('score pink', 'Started'), ('score green', 'Upcoming')], default='Upcoming', max_length=16),
        ),
    ]

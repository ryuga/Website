# Generated by Django 3.0.7 on 2020-07-07 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serverutils',
            old_name='suggestions',
            new_name='suggestion_message_id',
        ),
    ]

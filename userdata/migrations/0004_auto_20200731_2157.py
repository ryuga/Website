# Generated by Django 3.0.7 on 2020-07-31 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0003_serverutils_suggestions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serverutils',
            name='API_Gateway',
        ),
        migrations.RemoveField(
            model_name='serverutils',
            name='Github_Microservice',
        ),
        migrations.RemoveField(
            model_name='serverutils',
            name='Sockets',
        ),
        migrations.RemoveField(
            model_name='serverutils',
            name='Status_Microservice',
        ),
        migrations.RemoveField(
            model_name='serverutils',
            name='Tortoise_BOT',
        ),
        migrations.RemoveField(
            model_name='serverutils',
            name='Tortoise_BOT2',
        ),
        migrations.RemoveField(
            model_name='serverutils',
            name='Website',
        ),
        migrations.AlterField(
            model_name='projects',
            name='status',
            field=models.CharField(choices=[('cata red', 'Started'), ('cata green', 'Upcoming'), ('cata yellow', 'Completed'), ('cata purple', 'Refactoring')], default='Upcoming', max_length=16),
        ),
    ]
# Generated by Django 3.0.7 on 2020-10-17 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0004_auto_20201015_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infractions',
            name='warning',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='infraction', to='userdata.MemberWarning'),
        ),
        migrations.AlterField(
            model_name='rules',
            name='name',
            field=models.CharField(default='Rule name', max_length=20),
        ),
        migrations.AlterField(
            model_name='rules',
            name='number',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='rules',
            name='statement',
            field=models.TextField(blank=True),
        ),
    ]
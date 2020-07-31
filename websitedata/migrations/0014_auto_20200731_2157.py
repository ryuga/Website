# Generated by Django 3.0.7 on 2020-07-31 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websitedata', '0013_auto_20200708_0321'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='style',
            field=models.CharField(choices=[('Dark', 'dark.min.css'), ('Dracula', 'dracula.min.css'), ('Tomorrow', 'tomorrow.min.css'), ('Night Owl', 'night-owl.min.css'), ('Codepen', 'codepen-embed.min.css'), ('Github Gist', 'github-gist.min.css'), ('Atom Dark', 'atom-one-dark.min.css'), ('Solarized Dark', 'solarized-dark.min.css'), ('Atelier Cave', 'atelier-cave-dark.min.css'), ('Tomorrow Night Blue', 'tomorrow-night-blue.css'), ('Atom Dark Reasonable', 'atom-one-dark-reasonable.min.css')], default='default.min.css', max_length=25),
        ),
        migrations.AlterField(
            model_name='events',
            name='eventtype',
            field=models.CharField(choices=[('Other Event', 'Other'), ('CTF Event', 'CTF-Event'), ('Team Challenge', 'Team-Challenge'), ('Coding Challenge', 'Coding-Challenge')], default='CTF-Event', max_length=17),
        ),
        migrations.AlterField(
            model_name='events',
            name='status',
            field=models.CharField(choices=[('Live', 'Live'), ('Ended', 'Ended'), ('Upcoming', 'Upcoming')], default='Ended', max_length=17),
        ),
        migrations.AlterField(
            model_name='news',
            name='choice',
            field=models.CharField(choices=[('News', 'News'), ('Live', 'Live'), ('Announcements', 'Announcements')], default='Live', max_length=15),
        ),
    ]

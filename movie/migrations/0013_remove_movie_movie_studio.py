# Generated by Django 3.2.3 on 2021-06-17 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0012_alter_movie_movie_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='movie_studio',
        ),
    ]

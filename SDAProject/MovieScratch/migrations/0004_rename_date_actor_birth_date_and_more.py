# Generated by Django 4.2.5 on 2023-10-07 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MovieScratch', '0003_remove_movie_director_movie_directors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actor',
            old_name='date',
            new_name='birth_date',
        ),
        migrations.RenameField(
            model_name='director',
            old_name='date',
            new_name='birth_date',
        ),
    ]
# Generated by Django 4.2.5 on 2023-10-07 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieScratch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='directors',
            field=models.ManyToManyField(blank=True, related_name='directors_worked_with', to='MovieScratch.director'),
        ),
    ]

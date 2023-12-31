# Generated by Django 4.2.5 on 2023-10-06 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('release_date', models.DateField()),
                ('genres', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=500, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('actors', models.ManyToManyField(blank=True, related_name='movies_acted_in', to='MovieScratch.actor')),
                ('director', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movies_directed', to='MovieScratch.director')),
            ],
        ),
    ]

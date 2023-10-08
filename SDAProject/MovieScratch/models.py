from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    date = models.DateField()

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    date = models.DateField()  # Corrected 'Datefield' to 'DateField'

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=30)
    release_date = models.DateField()
    genres = models.CharField(max_length=25)
    description = models.CharField(max_length=500, null=True)
    rating = models.FloatField(blank=True, null=True)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, blank=True, related_name='movies_directed')
    actors = models.ManyToManyField(Actor, related_name='movies_acted_in', blank=True)

    def __str__(self):
        return self.title
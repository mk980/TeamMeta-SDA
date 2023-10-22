from django.shortcuts import get_object_or_404, render

from .models import Movie


# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, "index.html", {"movies": movies})


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, "movie_detail.html", {"movie": movie})

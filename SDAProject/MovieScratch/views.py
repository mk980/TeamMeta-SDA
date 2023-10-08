from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import Actor, Director, Movie

# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})


def index(request):
	query = request.GET.get('q')

	if query:
		url = 'http://www.omdbapi.com/?apikey=7239edb5&s=' + query
		response = request.get(url)
		movie_data = response.json()

		context = {
			'query': query,
			'movie_data': movie_data
		}

        template = loader.get_template('search_results.html')
        
        return HttpResponse(template.render(context, request))

	return render(request, 'index.html')

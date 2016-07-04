from django.shortcuts import render
from django.conf import settings

import requests

from .forms import MovieEmbed

from .serializers import MovieSerializer


def movie_embed(request):
    if request.method == 'POST':
        form = MovieEmbed(request.POST)
        if form.is_valid():
            imdbID = form.cleaned_data['imdbID']
            r = requests.get(
                'http://www.omdbapi.com/?' +
                'i=' + imdbID + '&plot=full&r=json')
            data = dict((k.lower(), v) for k,v in r.json().items())
            serializer = MovieSerializer(data=data)

            if serializer.is_valid():
                movie = serializer.save()
                return render(request, 'movie.html', {'movie': movie})
        # else:
        # 	print (serializer.errors)
    else:
        form = MovieEmbed()

    return render(request, 'index.html', {'form': form})

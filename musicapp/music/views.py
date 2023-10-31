from django.shortcuts import render
from .models import MusicBand, MusicGenre


def main_page(request):
    data = MusicGenre.objects.all()
    return render(request, 'music/index_main.html', {'data': data})


def bands_page(request, genre):
    find = MusicGenre.objects.get(genre=genre).pk
    data = MusicBand.objects.filter(genre=find)
    return render(request, 'music/index_bands.html', {'data': data})


def info_page(request, genre, slug):
    find = MusicGenre.objects.get(genre=genre).pk
    data = MusicBand.objects.filter(genre=find).get(slug=slug)
    return render(request, 'music/index_info.html', {'data': data})

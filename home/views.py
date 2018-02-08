from django.shortcuts import render, get_object_or_404
from .models import Artist
# Create your views here.

def artist_list_view(request):
	artists = Artist.objects.all()

	return render(request, 'index.html', {'artists': artists})

def artist_detail_view(request, slug):
	artist = get_object_or_404(Artist, slug=slug)

	return render(request, 'artist_detail.html', {'artist': artist}) 

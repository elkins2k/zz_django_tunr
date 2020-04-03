from django.shortcuts import render, redirect
from .models import Artist, Song
from .forms import ArtistForm, SongForm

def artist_list(req):
    artists = Artist.objects.all()
    return render(req, 'tunr/artist_list.html', {'artists': artists})

def artist_detail(req, pk):
    artist = Artist.objects.get(id=pk)
    return render(req, 'tunr/artist_detail.html', {'artist': artist})

def artist_delete(req, pk):
    Artist.objects.get(id=pk).delete()
    return redirect('artist_list')

def artist_create(req):
    if req.method == 'POST':
        form = ArtistForm(req.POST)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm()
    return render(req, 'tunr/artist_form.html', {'form': form})

def artist_edit(req, pk):
    artist = Artist.objects.get(pk=pk)
    if req.method == "POST":
        form = ArtistForm(req.POST, instance=artist)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm(instance=artist)
    return render(req, 'tunr/artist_form.html', {'form': form})

def song_list(req):
    songs = Song.objects.all()
    return render(req, 'tunr/song_list.html', {'songs': songs})

def song_detail(req, pk):
    song = Song.objects.get(id=pk)
    return render(req, 'tunr/song_detail.html', {'song': song})

def song_delete(req, pk):
    Song.objects.get(id=pk).delete()
    return redirect('song_list')

def song_create(req):
    if req.method == 'POST':
        form = SongForm(req.POST)
        if form.is_valid():
            song = form.save()
            return redirect('song_detail', pk=song.pk)
    else:
        form = SongForm()
    return render(req, 'tunr/song_form.html', {'form': form})

def song_edit(req, pk):
    song = Song.objects.get(pk=pk)
    if req.method == "POST":
        form = SongForm(req.POST, instance=song)
        if form.is_valid():
            song = form.save()
            return redirect('song_detail', pk=song.pk)
    else:
        form = SongForm(instance=song)
    return render(req, 'tunr/song_form.html', {'form': form})


from django.shortcuts import render, redirect
from .models import Songs
from .forms import LyricInsertForm
from .web_scraping import get_billboard100
from django.contrib.auth.decorators import login_required
# Create your views here.
def getSongList(request):
    Songs.objects.all().delete()
    for song in get_billboard100():
        Songs.objects.create(title=song['title'],artist=song['artist'],rank=song['rank'])
    songs=Songs.objects.all()
    return render(request,"Board/ChartList.html",{'billboard':songs})

def getSongDetail(request,rank):
    song=Songs.objects.get(rank=rank)
    return render(request,"Board/SongDetail.html",{'songInfo':song})

@login_required
def insertLyric(request,rank):
    song=Songs.objects.filter(rank=rank)
    if request.method == "POST":
        form = LyricInsertForm(request.POST)
        if form.is_valid():
            lyric = form.save(commit=False)
            lyric.song=song
            lyric.save()
            return redirect('song_detail',song.rank)
    else:
        form = LyricInsertForm()
        return render(request, 'Board/LyricInsert.html')

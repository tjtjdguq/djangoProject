from django.shortcuts import render
from .models import Songs
from .web_scraping import get_billboard100
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
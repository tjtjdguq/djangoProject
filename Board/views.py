from django.shortcuts import render
from .models import Songs
# Create your views here.
def getSongList(request):
    songs=Songs.objects.all()
    return render(request,"Board/ChartList.html",{'billboard':songs})

def getSongDetail(request):
    song=
    return render(request,"Board/SongDetail.html",{'songInfo'})
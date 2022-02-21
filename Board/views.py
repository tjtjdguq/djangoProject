from django.shortcuts import render, redirect
from .models import Songs,LyricInsert
from .forms import LyricInsertForm
from .web_scraping import get_billboard100
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
# Create your views here.
def getSongList(request):
    Songs.objects.all().delete()
    for song in get_billboard100():
        Songs.objects.create(title=song['title'],artist=song['artist'],rank=song['rank'])
    songs=Songs.objects.all()
    return render(request,"Board/ChartList.html",{'billboard':songs})

def getSongDetail(request,rank):
    song=Songs.objects.get(rank=rank)
    lyric_candidate=LyricInsert.objects.filter(song==song)
    return render(request,"Board/SongDetail.html",{'songInfo':song,'lyrics':lyric_candidate})

@login_required
def insertLyric(request,rank):
    song=Songs.objects.filter(rank=rank)
    if request.method == "POST":
        inst=LyricInsert()
        inst.song=song[0]
        inst.author=request.user
        form = LyricInsertForm(request.POST,instance=inst)
        if form.is_valid():
            lyric = form.save(commit=False)
            lyric.save()
            return redirect('song_detail',song[0].rank)
    else:
        form = LyricInsertForm()
    return render(request, 'Board/LyricInsert.html',{'form':form})

def signup(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request, 'Board/registration/signup.html', {'form': form})

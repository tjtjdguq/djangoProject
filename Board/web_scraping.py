from bs4 import BeautifulSoup
import requests

def get_billboard100():
    res = requests.get('https://www.billboard.com/charts/hot-100/')
    if res.ok:
        soup = BeautifulSoup(res.text, 'html.parser')
        songTitle = soup.select('li.lrv-u-width-100p ul li h3#title-of-a-story')
        Artists = soup.select('li.lrv-u-width-100p ul li h3#title-of-a-story+span')
        images = soup.select("li.o-chart-results-list__item div div img")
        songs = []
        for idx, song in enumerate(zip(songTitle, Artists, images), 1):
            songs.append({'rank': idx, 'title': song[0].text.strip(), 'artist': song[1].text.strip()})
        return songs
def find_web_with_lyrics(songs):
    lyric_pages = []
    for song in songs:
        query = song[1].replace(' ', '+')
        req = requests.get('https://search.azlyrics.com/search.php?q=' + query)
        if req.ok:
            soup = BeautifulSoup(req.text, 'html.parser')
            song_result = soup.select('div.panel-heading b')
            if (song_result and song_result[0].text == 'Song results:'):
                title_list = soup.select('div.panel-heading+table a span>b')
                artist_list = soup.select('div.panel-heading+table a span+b')
                if ((title_list[0].text.strip('"') == song[1].strip()) and (
                        artist_list[0].text.strip() == song[2].strip())):
                    links = soup.select("div.panel table a")
                    print(links[0]['href'])
                else:
                    print('artist no match')
            else:
                print('no song')
    return lyric_pages
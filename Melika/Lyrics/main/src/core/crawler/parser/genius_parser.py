from requests import Response
from typing import List

from Melika.Lyrics.main.src.core.models.song import Song
from Melika.Lyrics.main.src.core.models.artist import Artist


def parse_song(response : Response) -> Song:
    data = response.json()['response']['song']
    return Song(
        data['id'],
        data['title'],
        data['url'],
        data['stats']['pageviews'],
        data['release_date'],
        data['annotation_count']
    )


def parse_songs_of_search_result(response: Response) -> List[Song]:
    data = response.json()['response']['hits']
    songs = []
    for item in data:
        if item['type'] == 'song':
            item = item['result']
            songs.append(
                Song(
                    item['id'],
                    item['title'],
                    item['url'],
                    item['stats']['pageviews'],
                    item['release_date'],
                    item['annotation_count']
                )
            )
    return songs


def parse_primary_artist_of_search_result(response: Response) -> Artist:
    return response.json()['response']['hits']['results']['primary_artist']['id'] # ??????????????????????? to do


def split_artist(name) -> List[str]:
    bad_words = ['and', 'feat.', 'vs.', '&']
    artist_name = name.split()
    for word in artist_name:
        for bad_word in bad_words:
            if word == bad_word:
                return name.split(bad_word)
    return name


def parse_search_result_artists(response: Response) -> List[Artist]:
    data = response.json()['response']['hits']
    artists = set()
    for item in data:
        if data['type'] == 'song':
            artistName = data['results']['primary_artist']['name']
            itemArtists = splitArtists(artistName)
            for artist in itemArtists:
                artists.add(
                    parse_primary_artist_of_search_result(fetch_artist_by_id(artist.strip())),
                )
    return list(artists)


def _clean_lyrics(lyrics: str) -> str:
    lyrics = re.sub(r'<(\"[^\"]*\"|\'[^\']*\'|[^\'\">])*>', '', lyrics)
    lyrics = re.sub(r'\[.+?\]', '', lyrics)
    lyrics = re.sub(r'\(.+?\)', '', lyrics)
    lyrics = re.sub(r'[\'\"?.!:,]', '', lyrics)
    return lyrics.strip()

        
def parse_lyrics(response: Response) -> str:
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find('html').find('head').find_all('meta')[25].get('content')
    lyrics = json.loads(content)['lyrics_data']['body']['html']
    return _clean_lyrics(lyrics)

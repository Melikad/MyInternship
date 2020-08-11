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

def parse_search_result_songs(response: Response) -> List[Song]:
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

    
def parse_search_artist(response: Response) -> str:
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
                    Artist(
                        parse_search_artist(fetch_artist_by_id(artist.strip())),
                        artist
                    )
                )
    return artists

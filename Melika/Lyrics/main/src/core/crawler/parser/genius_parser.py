# Standard Library
from typing import List

# Site packages
from requests import Response
from bs4 import BeautifulSoup

# Internal
from Melika.Lyrics.main.src.core.models.song import Song
from Melika.Lyrics.main.src.core.models.artist import Artist


def parse_song(response : Response) -> Song:
    """
        @param response: fetch_song response
    """
    data = response.json()['response']['song']
    return Song(
        data['id'],
        data['title'],
        data['url'],
        data['stats']['pageviews'],
        data['release_date'],
        data['annotation_count']
    )


def parse_artist_songs(response: Response) -> List[Song]:
    """
        @param response: fetch_artist_songs response
    """
    data = response.json()['response']['songs']
    songs = {
        Song(
            song['id'],
            song['title'],
            song['url'],
            int(song['stats']['pageviews']) if 'stats' in song and 'pageviews' in song['stats'] else None,
            None,
            int(song['annotation_count']),
        )
        for song in data
    }
    return list(songs)


def parse_search_results_songs(response: Response) -> List[Song]:
    """
        @param response: fetch_search_results response
    """
    data = response.json()['response']['hits']
    songs = set()
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
    return list(songs)


def parse_artist_id(response: Response) -> str:
    """
        @param response: fetch_search_results response
    """
    return response.json()['response']['hits']['results']['primary_artist']['id']


def parse_search_result_artists(response: Response) -> List[Artist]:
    """
        @param response: fetch_search_results response
    """
    data = response.json()['response']['hits']
    artists = {
        Artist(
            item['result']['primary_artist']['id'],
            item['result']['primary_artist']['name']
        )
        for item in data
        if item['type'] == 'song'
    }
    return list(artists)


def _clean_lyrics(lyrics: str) -> str:
    """
        @param lyrics: songs lyrics
        @return str: clean version of the lyrics
    """
    lyrics = re.sub(r'<(\"[^\"]*\"|\'[^\']*\'|[^\'\">])*>', '', lyrics)
    lyrics = re.sub(r'\[.+?\]', '', lyrics)
    lyrics = re.sub(r'\(.+?\)', '', lyrics)
    lyrics = re.sub(r'[\'\"?.!:,]', '', lyrics)
    return lyrics.strip()


def parse_lyrics(response: Response) -> str:
    """
        @param lyrics_response
        @return str: extracted lyrics
    """
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find('html').find('head').find_all('meta')[25].get('content')
    lyrics = json.loads(content)['lyrics_data']['body']['html']
    return _clean_lyrics(lyrics)

# Standard Library
from typing import List, Dict, Any, Union

# Site Packages
import requests

# Internal
from Melika.Lyrics.src.core.models.artist import Artist
from Melika.Lyrics.src.core.models.song import Song


def _gather_top_hit_song_from_hits(hits: List[Dict[str, Any]]) -> Song:
    top_hit_song = hits[0]['result']
    return Song(
            top_hit_song['id'], top_hit_song['title'], '', Artist(
            top_hit_song['primary_artist']['id'],
            top_hit_song['primary_artist']['name']
        ),
        top_hit_song['url']
    )

def get_genius_results(query: str) -> Union[Song, None]:
    response = requests.get('https://genius.com/api/search/multi', params={'q': query})
    data = response.json()['response']['sections']
    for result in data:
        if result['type'] == 'song':
            return _gather_top_hit_song_from_hits(result['hits'])
    return None

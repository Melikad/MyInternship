from requests import Response
from typing import List

from Melika.Lyrics.main.src.core.models.song import Song

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




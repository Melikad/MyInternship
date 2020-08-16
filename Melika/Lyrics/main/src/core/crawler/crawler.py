from Melika.Lyrics.main.src.core.crawler.fetcher.genius_fetcher import GeniusFetcher
from Melika.Lyrics.main.src.core.crawler.parser.genius_parser import *
from Melika.Lyrics.main.src.core.crawler.submitter.submitter import SqliteSubmitter
from Melika.Lyrics.main.src.core.models.artist import Artist
from Melika.Lyrics.main.src.core.models.song import Song

from typing import List


class GeniusCrawler:
    
    __slots__ = 'fetcher', 'submitter'
    
    def __init__(self, fetcher: GeniusFetcher, submitter: SqliteSubmitter):
        self.fetcher = fetcher
        self.submitter = submitter
    
    # def get_artist_words(self, artist_name: str) -> None:
    #     fetcher = GeniusFetcher(10, 10, 10, token)
    #     songs = parse_search_result_songs(fetcher.fetch_artist_id(artist_name))

    def get_artist_id(self, artist_name: str) -> str:
        return parse_search_result_artists(self.fetcher.fetch_search_results(artist_name))[0].id

    def get_artist_ids(self, artist_names: List[str]) -> List[str]:
        return [self.get_artist_id(artist_name) for artist_name in artist_names]
    
    def get_artist_songs(self, artist_id: str) -> List[Song]:
        return parse_artist_songs(
            self.fetcher.fetch_artist_songs(
                artist_id,
                sort = 'title',
                per_page = 30,
                page = 1
            )
        )
        
    def get_artists_songs(self, artist_ids: List[str]) -> List[List[Song]]:
        return [ self.get_artist_songs(artist_id) for artist_id in artist_ids ]

    def crawl(self, artist_names: List[str]) -> None:
        ids = self.get_artist_ids(artist_names)
        songs_list = self.get_artists_songs(ids)
        
        integrated_songs = [] 
        for songs in songs_list:
            integrated_songs += songs

        integrated_songs = list(set(integrated_songs))
        
        self.submitter.submit('songs', integrated_songs)

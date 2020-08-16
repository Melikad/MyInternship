# Standard Library
from typing import Union

# Site Packages
from requests import Response, Request

# Internal
from .fetcher import Fetcher, Session


class GeniusFetcher(Fetcher):

    __slots__ = '_token',

    api_url = 'https://api.genius.com/'
    website_url = 'https://genius.com/api/'

    def __init__(self, max_attempts: int, failed_sleep_time: Union[float, int], timeout: Union[float, int],
                 token: str):
        super().__init__(max_attempts, failed_sleep_time, timeout)
        self._token = token
        self._init_session()
        print('[GeniusFetcher] Init')
    
    def _init_session(self) -> None:
        session: Session = Session()
        session.headers = {
            'application': 'MelikaLyrics',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
            'authorization': 'Bearer ' + self._token
        }
        self.session = session

    # Tested
    def fetch_song(self, song_id: str) -> Response:
        print(f'Fetching song: id={song_id}')
        request = Request('GET', url=self.api_url + f'songs/{song_id}')
        return self._fetch(request)

    # Tested
    def fetch_search_results(self, query: str) -> Response:
        print(f'Fetching Search Results: query={query}')
        request = Request('GET', url=self.api_url + 'search', params={'q': query})
        return self._fetch(request)

    # Tested
    def fetch_artist_songs(self, artist_id: str, sort = 'title', per_page: int = 20, page: int = 1) -> Response:
        print(f'Fetching Artist Songs: id={artist_id}')
        print(f'Fetching Songs of Artist : ({artist_id})')
        request = Request(
            'GET',
            url=self.api_url + f'artists/{artist_id}/songs',
            params={
                'sort': sort,
                'per_page': per_page,
                'page': page
            }
        )
        return self._fetch(request)

    # Tested
    def fetch_song_lyrics(self, url: str) -> Response:
        request = Request(
            'GET',
            url = self.website_url + url
        )
        return self._fetch(request)

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
    
    def _init_session(self) -> None:
        session: Session = Session()
        session.headers = {
            'application': 'MelikaLyrics',
            'User-Agent': 'Mozilla',
            'authorization': 'Bearer ' + self._token
        }
        self.session = session
    
    def fetch_song(self, song_id: str) -> Response:
        print('search song *******************')
        request = Request('GET', url=self.api_url + f'songs/{song_id}')
        return self._get(request)

    def fetch_search_results(self, query: str) -> Response:
        request = Request('GET', url=self.api_url + 'search', params={'q': query})
        return self._get(request)

    def fetch_artist_songs(self, artist_id: str, sort = 'title', per_page: int = 20, page: int = 1) -> Response:
        request = Request(
            'GET',
            url=self.api_url + f'artists/{artist_id}/songs',
            params={
                'sort': sort,
                'per_page': per_page,
                'page': page
            }
        )
        return self._get(request)

    def fetch_song_lyrics(self, url: str) -> Response:
        request = Request(
            'GET',
             url = self.website_url + url
        )
        return self._get(request)


    def fetch_artist_id(self, name: str) -> str:
        request = Request('GET', url=self.api_url + 'search', params={'q': name})
        return self._get(request)
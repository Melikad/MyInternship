from Melika.Lyrics.main.src.core.crawler.fetcher.genius_fetcher import GeniusFetcher
from Melika.Lyrics.main.src.core.crawler.parser.genius_parser import *

"""
class Crawler:
    __slots__ = 'fetcher',

token = 'U4R1EqqxfejlD_WC_MCkDIvbZ0cLsFnvaCVFd8-mxUI16a0-mZ3Vrdh7Ecp_h1iW'
fetcher = GeniusFetcher()

def get_artist_words(artist_name):
    fetcher = GeniusFetcher(10, 10, 10, token)
    songs = parse_search_result_songs(fetcher.fetch_artist_id(artist_name))

def find_artist_id(artist_name):
    artists = parse_search_result_artists(fetcher.fetch_search_results(artist_name))
    for artist in artists:
        if artist.get_name() == artist_name:
            return artist

def find_lyrics(artist_name):
    songs = parse_search_result_songs(fetcher.fetch_artist_songs(find_artist_id(artist_name)))


def get_artists(file_name):
    file = open(file_name, "r")
    for i in range (10):
        artist = file.read()
        find_lyrics(artist)


# input = Artist
# ArtistName -> ArtistId ( search )
# ArtistId -> All Songs  ( fetch_artist_songs )
# Song -> Lyrics
# output = Lyrics of all songs of artists
get_artists('artists.txt')
"""
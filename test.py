from Melika.Lyrics.main.src.core.crawler.fetcher.genius_fetcher import GeniusFetcher
from Melika.Lyrics.main.src.core.crawler.parser.genius_parser import *

token = 'U4R1EqqxfejlD_WC_MCkDIvbZ0cLsFnvaCVFd8-mxUI16a0-mZ3Vrdh7Ecp_h1iW'

def get_artist_words(artist_name):
    fetcher = GeniusFetcher(10, 10, 10, token)
    songs = parse_search_result_songs(fetcher.fetch_artist_id(artist_name))


def get_artist(file_name):
    file = open(file_name, "r")
    print(file.read())

fetcher = GeniusFetcher(10, 10, 10, token)
response = fetcher.fetch_artist_id('bad guy')

with open('output.json', 'w', encoding='utf8') as file:
    file.write(response.text)
from Melika.Lyrics.main.src.core.crawler.fetcher.genius_fetcher import GeniusFetcher
from Melika.Lyrics.main.src.core.crawler.parser.genius_parser import *
from Melika.Lyrics.main.src.core.crawler.crawler import GeniusCrawler
from Melika.Lyrics.main.src.core.models.song import Song
from Melika.Lyrics.main.src.core.crawler.submitter.submitter import SqliteSubmitter
from Melika.Lyrics.main.src.core.crawler.crawler import GeniusCrawler
import sqlite3

token = 'U4R1EqqxfejlD_WC_MCkDIvbZ0cLsFnvaCVFd8-mxUI16a0-mZ3Vrdh7Ecp_h1iW'
fetcher = GeniusFetcher(max_attempts=10, failed_sleep_time=2, timeout=10, token=token)
submitter = SqliteSubmitter('Genius.db')
crawler = GeniusCrawler(fetcher, submitter)

crawler.crawl([
    'billie eilish',
    'mumford and sons',
    'birdy',
    'queen',
    'imagine dragons',
    'aaron',
    'najafi',
    'tom odell',
    'sia',
    'led zapplin'
])

# def make_table(db_name):
#     connection = sqlite3.connect(db_name)
#     connection.execute(
#         """
#         CREATE TABLE "songs" (
#             id TEXT PRIMARY KEY,
#             title TEXT,
#             url TEXT,
#             views INTEGER,
#             release_date TEXT,
#             annotations TEXT,
#             lyrics TEXT
#         );
#         """
#     )
#     connection.commit()

# make_table('Genius.db')
# response = fetcher.fetch_song_lyrics('https://genius.com/Billie-eilish-and-khalid-lovely-lyrics')

# with open('lyrics.json', 'w', encoding='utf8') as file:
#     file.write(response.text)


# from Melika.Lyrics.main.src.core.crawler.submitter.submitter import Model
# from Melika.Lyrics.main.src.core.crawler.submitter.submitter import SqliteSubmitter
# import sqlite3

# class Contact(Model):
    
#     __slots__ = 'phone', 'id', 'name'
    
#     def __init__(self, id_: int, name: str, phone: str):
#         super().__init__(id_)
#         self.phone = phone
#         self.name = name
        



# contacts = [Contact(1, "ahmad", "09322422"), Contact(2, "asghar", "98989833")]

# #make_table('melika.db')

# 1. Artist List
# 2. Artist -> ArtistId
# 3. ArtistId -> SongList

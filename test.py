# from Melika.Lyrics.main.src.core.crawler.fetcher.genius_fetcher import GeniusFetcher
# from Melika.Lyrics.main.src.core.crawler.parser.genius_parser import *

# token = 'U4R1EqqxfejlD_WC_MCkDIvbZ0cLsFnvaCVFd8-mxUI16a0-mZ3Vrdh7Ecp_h1iW'

# def get_artist_words(artist_name):
#     fetcher = GeniusFetcher(10, 10, 10, token)
#     songs = parse_search_result_songs(fetcher.fetch_artist_id(artist_name))

# def get_artist(file_name):
#     file = open(file_name, "r")
#     print(file.read())

# fetcher = GeniusFetcher(10, 10, 10, token)
# response = fetcher.fetch_search_results('billie eilish')

# with open('output.json', 'w', encoding='utf8') as file:
#     file.write(response.text)


from Melika.Lyrics.main.src.core.crawler.submitter.submitter import Model
from Melika.Lyrics.main.src.core.crawler.submitter.submitter import SqliteSubmitter
import sqlite3


# def make_table(db_name):
#     connection = sqlite3.connect(db_name)
#     connection.execute(
#         """
#         CREATE TABLE "contacts" (
#             id INTEGER PRIMARY KEY,
#             name TEXT NOT NULL,
#             phone TEXT NOT NULL UNIQUE
#         );
#         """
#     )
#     connection.commit()


class Contact(Model):
    
    __slots__ = 'phone', 'id', 'name'
    
    def __init__(self, id_: int, name: str, phone: str):
        super().__init__(id_)
        self.phone = phone
        self.name = name
        



contacts = [Contact(1, "ahmad", "09322422"), Contact(2, "asghar", "98989833")]
submitter = SqliteSubmitter('melika.db')
#make_table('melika.db')
submitter.submit('contacts', contacts)

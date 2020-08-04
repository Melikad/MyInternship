# Internal
from Melika.Lyrics.src.utils.string_utils import SlotString
from Melika.Lyrics.src.core.models.artist import Artist


class Song(SlotString):

    __slots__ = 'id', 'title', 'artist', 'url'

    def __init__(self, id_: str, title: str, artist: Artist, url: str):
        self.id = id_
        self.title = title
        self.artist = artist
        self.url = url

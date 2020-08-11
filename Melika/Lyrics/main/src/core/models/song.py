# Internal
from Melika.Lyrics.main.src.utils.string_utils import SlotString
from Melika.Lyrics.main.src.core.models.artist import Artist


class Song(SlotString):

    __slots__ = 'id', 'title', 'url', 'views', 'release_date', 'annotations'

    def __init__(self, id_: str, title: str, url: str, views: int, date: str, annotations: int):
        self.id = id_
        self.title = title
        self.url = url
        self.views = views
        self.release_date = date
        self.annotations = annotations

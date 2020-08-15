# Standard Library
from typing import Optional

# Internal
from Melika.Lyrics.main.src.core.models.model import Model


class Song(Model):

    __slots__ = 'id', 'title', 'url', 'views', 'release_date', 'annotations', 'lyrics'

    def __init__(self, id_: str, title: str, url: str, views: int, date: str,
                 annotations: int, lyrics: Optional[str] = None):
        super().__init__(id_)
        self.title = title
        self.url = url
        self.views = views
        self.release_date = date
        self.annotations = annotations
        self.lyrics = lyrics

# Internal
from Melika.Lyrics.main.src.core.models.model import Model


class Artist(Model):
    
    __slots__ = 'id', 'name'

    def __init__(self, id_: str, name: str):
        super().__init__(id_)
        self.name = name

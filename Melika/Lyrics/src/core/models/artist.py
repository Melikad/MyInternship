# Internal
from Melika.Lyrics.src.utils.string_utils import SlotString


class Artist(SlotString):
    
    __slots__ = 'id', 'name'

    def __init__(self, id_: str, name: str):
        self.id = id_
        self.name = name

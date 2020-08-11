# Internal
from Melika.Lyrics.main.src.utils.string_utils import SlotString


class Artist(SlotString):
    
    __slots__ = 'id', 'name'

    def __init__(self, id_: str, name: str):
        self.id = id_
        self.name = name

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return (
            self.__class__ == other.__class__ and
            self.id == other.id
        )

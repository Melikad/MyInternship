# Standard Library
from abc import ABC


class SlotString(ABC):

    def __str__(self) -> str:
        return type(self).__name__ + '(' + ', '.join(
            [
                f'{attr}: {self.__getattribute__(attr)}'
                for attr in self.__slots__
            ]
        ) + ')'

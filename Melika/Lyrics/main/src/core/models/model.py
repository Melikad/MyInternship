# Standard Library
from abc import ABC
from typing import Union


class Model(ABC):
    
    __slots__ = 'id',
    
    def __init__(self, id_: Union[int, float, str]):
        self.id = id_
    
    def __str__(self) -> str:
        return type(self).__name__ + '(' + ', '.join(
            [
                f'{attr}: {self.__getattribute__(attr)}'
                for attr in self.__slots__
                if self.__getattribute__(attr) is not None
            ]
        ) + ')'
        
    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return self.id.__hash__()
    
    def __eq__(self, other):
        return ( other.__class__ == self.__class__ and other.id == self.id)

# Standard Library
from abc import ABC, abstractmethod
from typing import Set, List, Union
from sqlite3 import Connection as SqliteConnection

# Internal
from Melika.Lyrics.main.src.core.models.model import Model


class Submitter(ABC):

    @abstractmethod
    def submit(table:str, model_collection: Set[Model]) -> None:
        pass


class SqlDataBaseSubmitter(Submitter, ABC):
    
    __slots__ = '_connection', '_url'
    
    @abstractmethod
    def _build_insert_query(self, table: str, model_collection: Set[Model]) -> str:
        pass


class SqliteSubmitter(SqlDataBaseSubmitter, ABC):
        
    def __init__(self, db_url: str):
        self._url = db_url
        self._connection = SqliteConnection(db_url)
    
    @staticmethod
    def _to_str(value: Union[float, int, str]):
        if type(value) is float:
            return str(value)
        if type(value) is int:
            return str(value)
        if type(value) is str:
            return f'"{value}"'
        raise ValueError(f'Value must be int/float/str, but was {type(value)}')
        
    def _build_insert_query(self, table: str, model_collection: List[Model]) -> str:
        columns = model_collection[0].__slots__
        values = ', '.join(
            [
                '(' + ', '.join([self._to_str(getattr(model, col)) for col in columns]) + ')'
                for model in model_collection 
            ]
        )
        query = f'INSERT INTO {table} '\
                '(' + ', '.join(["\"" + col + "\"" for col in columns]) + ')' \
                f'VALUES {values};'
        return query
    
    def submit(self, table: str, model_collection: Set[Model]) -> None:
        query = self._build_insert_query(table, model_collection)
        self._connection.execute(query)
        self._connection.commit()

from typing import List
from abc import ABC, abstractmethod

class DAO(ABC):

    @abstractmethod
    def create_schema(self, schema : Sql):
        pass

    @abstractmethod
    def insert_words(self, resources : List[str]):
        pass

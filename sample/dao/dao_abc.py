from abc import ABC, abstractmethod
from sample.resources.lexical_resources import LexicalResources


class DAO(ABC):

    @abstractmethod
    def upload_words(self, resources: LexicalResources):
        pass


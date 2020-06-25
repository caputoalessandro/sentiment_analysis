from abc import ABC, abstractmethod
from sample.resources.resources import Resources


class DAO(ABC):

    @abstractmethod
    def upload_words(self, resources: Resources):
        pass

    @abstractmethod
    def upload_words_values(self, resources: Resources):
        pass

    @abstractmethod
    def upload_twitters(self, resources: Resources):
        pass
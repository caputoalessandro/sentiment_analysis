from abc import ABC, abstractmethod
from sample.resources.resources import Resources


class DAO(ABC):

    @abstractmethod
    def upload_words(self, resources: Resources):
        pass


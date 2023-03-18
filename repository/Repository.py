from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def create(self, item):
        pass

    @abstractmethod
    def read(self, id):
        pass
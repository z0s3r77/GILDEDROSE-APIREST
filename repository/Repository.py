from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def create(self, item):
        ...

    @abstractmethod
    def read(self, id):
        ...

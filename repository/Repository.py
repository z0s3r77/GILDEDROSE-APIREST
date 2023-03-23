from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def create(self, item):
        ...

    @abstractmethod
    def read(self, id):
        ...

    @abstractmethod
    def update(self, id, updatedItem):
        ...

    @abstractmethod
    def delete(self, id):
        ...

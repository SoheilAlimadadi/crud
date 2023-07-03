from abc import ABC, abstractmethod

class IDataAccessLayer(ABC):

    @abstractmethod
    def get_all(self, model):
        raise NotImplementedError

    @abstractmethod
    def get_one(self, model, phone_number):
        raise NotImplementedError

    @abstractmethod
    def create(self, model, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def update(self, phone_number, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def delete(self, phone_number):
        raise NotImplementedError

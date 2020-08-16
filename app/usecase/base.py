from abc import ABC, abstractmethod


class BaseUseCase(ABC):

    @abstractmethod
    def execute(self):
        return self.valid_data()

    @abstractmethod
    def valid_data(self):
        pass

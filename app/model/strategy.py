from abc import ABC, abstractmethod

class Strategy(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def buy(self):
        pass

    @abstractmethod
    def sell(self):
        pass

    @abstractmethod
    def update(self,value:dict):
        pass
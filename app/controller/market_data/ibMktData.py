from abc import ABC, abstractmethod
from typing import List

class IBMktData(ABC):
    def __init__(self,ibApp):
        super().__init__()
        self.app = ibApp
        self._observers = []

    @property
    def observers(self) -> List[object]:
        return self._observers
    
    @observers.setter
    def observers(self):
        pass

    @observers.deleter
    def observers(self):
        pass

    def attach(self,observer):
        self._observers.append(observer)
    
    def detach(self,observer):
        pass

    def notify(self):
        for observer in self._observers:
            observer.update()

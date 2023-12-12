from collections.abc import Callable
from concurrent.futures._base import Future

from ibapi.common import TickerId
from .wrapper import Wrapper
from .client import Client

class IBApi(Wrapper,Client):
    _instance = None
    _initialized = None
    def __init__(self):
        Wrapper.__init__(self)
        Client.__init__(self,wrapper=self)


    def run(self):
        print("*** Running app ***")
        future = self.executor.submit(fn=super().run)
        self._futures.update({'run':future})

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __delattr__(cls) -> None:
        cls._instance = None
        if not cls.isConnected():
            cls.disconnect()
        
        cls.executor.shutdown(wait=False)
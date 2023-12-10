from .wrapper import Wrapper
from .client import Client

class IBApp(Wrapper,Client):
    _instance = None
    def __init__(self):
        Wrapper.__init__(self)
        Client.__init__(self,wrapper=self)

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __delattr__(cls) -> None:
        cls._instance = None
        if not cls.isConnected():
            cls.disconnect()
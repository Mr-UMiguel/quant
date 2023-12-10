from ibapi.client import *

class Client(EClient):
    def __init__(self,wrapper):
        EClient.__init__(self,wrapper)

    def connect(self, host, port, clientId):
        print("Connection Established")
        return super().connect(host, port, clientId)
    
    def disconnect(self):
        print("Connection has been disconnected")
        return super().disconnect()
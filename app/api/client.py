from ibapi.client import *
from ibapi.common import TagValueList, TickerId
from ibapi.contract import Contract


from concurrent.futures import ThreadPoolExecutor

class Client(EClient):
    _futures = {}
    def __init__(self,wrapper):
        EClient.__init__(self,wrapper)
        self.executor = ThreadPoolExecutor(max_workers=4)

    @property
    def futures(self):
        return self._futures
    
    @futures.setter
    def futures(self,value):
        pass

    @futures.deleter
    def futures(self):
        pass

    def connect(self, host, port, clientId):
        print("Connection Established hola Lau")
        return super().connect(host, port, clientId)
    
    def disconnect(self):
        print("Connection has been disconnected chao Lau")
        if self._futures['run'].running():
            self._futures['run'].cancel()
        return super().disconnect()
    
    def reqIds(self, numIds: int):
        return numIds
    
    def reqMktData(self, reqId:int, contract: Contract):
        print("*** Starting real time market data ***")
        future =  self.executor.submit(fn=super().reqMktData, reqId= reqId, contract=contract,
                                        genericTickList="", snapshot= False, regulatorySnapshot= False, 
                                        mktDataOptions= [])
        self._futures.update({'mktData': future})
    
    def cancelMktData(self, reqId: TickerId):
        print("*** Cancelling real time market data ***")
        if self._futures['mktData'].running():
            self._futures['mktData'].cancel()

        return super().cancelMktData(reqId)
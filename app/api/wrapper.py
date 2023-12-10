from ibapi.wrapper import *
from typing import List
import json

class Wrapper(EWrapper):

    def __init__(self):
        EWrapper.__init__(self)
        self._observers = []

    @property
    def observers(self):
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
        self._observers.remove(observer)
    
    def notify(self,value:dict):
        for observer in self._observers:
            observer.update(value)

    def error(self, reqId: TickerId, errorCode: int, errorString: str, advancedOrderRejectJson=""):
        print("***")
        return super().error(reqId, errorCode, errorString, advancedOrderRejectJson)

    def nextValidId(self, orderId: int):
        return super().nextValidId(orderId)

    def currentTime(self, time: int):
        return super().currentTime(time)

    def pnlSingle(self, reqId: int, pos: Decimal, dailyPnL: float, unrealizedPnL: float, realizedPnL: float, value: float):
        return super().pnlSingle(reqId, pos, dailyPnL, unrealizedPnL, realizedPnL, value)

    def historicalData(self, reqId: int, bar: BarData):
        return super().historicalData(reqId, bar)
        
    def historicalDataEnd(self, reqId: int, start: str, end: str):
        return super().historicalDataEnd(reqId, start, end)
    
    def contractDetails(self, reqId: int, contractDetails: ContractDetails):
        return super().contractDetails(reqId, contractDetails)
    
    def sim_rtData(self,barData:dict):
        for i in barData:
            self.notify(i)

    def get_testVPrices(self) -> List[dict]:
        with open('source/testMktData.json','r') as file:
            data = json.load(file)
        
        return data

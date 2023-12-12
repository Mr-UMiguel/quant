from ibapi.common import Decimal, TickAttrib, TickerId
from ibapi.ticktype import TickType
from ibapi.utils import Decimal
from ibapi.wrapper import *
from typing import List
import json

class Wrapper(EWrapper):
    nextOrderID = 1
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
        print(reqId, errorCode, errorString, advancedOrderRejectJson)
        return super().error(reqId, errorCode, errorString, advancedOrderRejectJson)

    def nextValidId(self, orderId: int):
        self.nextOrderID = orderId
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
    

    def tickPrice(self, reqId: TickerId, tickType: TickType, price: float, attrib: TickAttrib):
        self.notify({'reqId':reqId, 'tickType':tickType, 'price':price, 'attrib': attrib})

    def sim_rtData(self,barData:dict):
        for i in barData:
            self.notify(i)

    def get_testVPrices(self) -> List[dict]:
        with open('source/testMktData.json','r') as file:
            data = json.load(file)
        
        return data

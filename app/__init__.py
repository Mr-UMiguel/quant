from ibapi.client import *
from ibapi.common import BarData, Decimal, OrderId, TickerId
from ibapi.contract import Contract
from ibapi.order import Order
from ibapi.order_state import OrderState
from ibapi.utils import Decimal
from ibapi.wrapper import *

import json
# import logging
# import os

# logging.basicConfig(
#     filename= os.path.join('..', 'debbug_app.log'),
#     level=logging.DEBUG,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )

class Wrapper(EWrapper):

    def __init__(self):
        EWrapper.__init__(self)

    def error(self, reqId: TickerId, errorCode: int, errorString: str, advancedOrderRejectJson=""):
        print("***")
        return super().error(reqId, errorCode, errorString, advancedOrderRejectJson)

    def nextValidId(self, orderId: int):
        print("+++")
        print(orderId)
        return super().nextValidId(orderId)
    

    def accountSummary(self, reqId: int, account: str, tag: str, value: str, currency: str):
        print("---AccountSummary---")
        print(reqId, account, tag, value, currency)
        self.disconnect()

    
    def openOrder(self, orderId: OrderId, contract: Contract, order: Order, orderState: OrderState):
        print("---openOrder---")
        print(orderId, contract, order, orderState)
        self.disconnect()


    def currentTime(self, time: int):
        print("---currentTime---")
        print(time)
        return super().currentTime(time)
    def pnlSingle(self, reqId: int, pos: Decimal, dailyPnL: float, unrealizedPnL: float, realizedPnL: float, value: float):
        print("---pnl---")
        print(reqId, pos, dailyPnL, unrealizedPnL, realizedPnL, value)
        return super().pnlSingle(reqId, pos, dailyPnL, unrealizedPnL, realizedPnL, value)

    def historicalData(self, reqId: int, bar: BarData):
        with open('source/testMktData.json', 'r+') as file:
            data = json.load(file)
            data.append({
                'reqid' : str(reqId),
                'date': bar.date,
                'open': str(bar.open),
                'high': str(bar.high),
                'low' : str(bar.low),
                'close': str(bar.close),
                'volume': str(bar.volume),
                'wap'  : str(bar.wap),
                'count': str(bar.barCount)
            })

            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()

        return super().historicalData(reqId, bar)
    
    def historicalDataEnd(self, reqId: int, start: str, end: str):
        print("---HistoricalDataEnd---")
        print(f"start:{start}, end:{end}")
        return super().historicalDataEnd(reqId, start, end)

class Client(EClient):
    def __init__(self,wrapper):
        EClient.__init__(self,wrapper)

    def connect(self, host, port, clientId):
        print("Connection Established")
        return super().connect(host, port, clientId)
    
    def disconnect(self):
        print("Connection has been disconnected")
        return super().disconnect()
    
    def l(cls):
        cls.reqPnLSingle()

class App(Wrapper,Client):
    _instance = None
    def __init__(self):
        Wrapper.__init__(self)
        Client.__init__(self,wrapper=self)

    # def contractDetails(self, reqId: int, contractDetails: ContractDetails):
    #     # logging.info(f"contract details: {contractDetails}")
    #     print(f"contract details: {contractDetails}")

    # def contractDetailsEnd(self, reqId: int):
    #     # logging.info("End of contractDetails")
    #     print("End of contractDetails")
    #     self.disconnect()


    # def nextValidId(self, orderId: int):
    #     mycontract = Contract()
    #     mycontract.symbol = "AAPL"
    #     mycontract.secType = "STK"
    #     mycontract.exchange = "SMART"
    #     mycontract.currency = "USD"
    #     self.reqHistoricalData(orderId, mycontract, "20221010 15:00:00 US/Eastern", "1 D", "1 hour", "TRADES", 0, 1, 0, [])

    # def historicalData(self, reqId: int, bar: BarData):
    #     print("starting historical data")
    #     print(bar)
    
    # def historicalDataEnd(self, reqId: int, start: str, end: str):
    #     print("End of historical Data")
    #     print(reqId, start, end)
    #     self.disconnect()


    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __delattr__(cls) -> None:
        cls._instance = None
        if not cls.isConnected():
            cls.disconnect()
        
    
    

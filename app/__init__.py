from ibapi.client import *
from ibapi.common import BarData
from ibapi.wrapper import *

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

class Client(EClient):
    def __init__(self,wrapper):
        EClient.__init__(self,wrapper)

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


    def nextValidId(self, orderId: int):
        mycontract = Contract()
        mycontract.symbol = "AAPL"
        mycontract.secType = "STK"
        mycontract.exchange = "SMART"
        mycontract.currency = "USD"
        self.reqHistoricalData(orderId, mycontract, "20221010 15:00:00 US/Eastern", "1 D", "1 hour", "TRADES", 0, 1, 0, [])

    def historicalData(self, reqId: int, bar: BarData):
        print("starting historical data")
        print(bar)
    
    def historicalDataEnd(self, reqId: int, start: str, end: str):
        print("End of historical Data")
        print(reqId, start, end)
        self.disconnect()

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
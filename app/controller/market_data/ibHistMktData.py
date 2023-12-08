from .ibMktData import IBMktData
from typing import *
from ibapi.wrapper import Contract


class IBHistMktData(IBMktData):

    def __init__(self,ibApp):
        IBMktData.__init__(self,ibApp)

    def request_contract(self,orderID:int,contract:Contract,
                        start_date:str, broll_date:str, freq:str, on:str):
        print(self.app)
        self.app.reqHistoricalData(orderID, contract,start_date, broll_date, freq, on,
                                    0, 1, 0, [])
        
    
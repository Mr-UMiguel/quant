from abc import ABC, abstractmethod
from .money_manager import MoneyManager
from .risk_manager import RiskManager
from .order_manager import OrderManager
from api.ibApi import IBApi

from ibapi.wrapper import Contract


class Strategy(ABC):

    def __init__(self,ibApi:IBApi,contract:Contract,moneyManager:MoneyManager,
                    orderManager:OrderManager, riskManager:RiskManager):
        
        self.ibApi = ibApi
        self._contract = contract
        self._moneyManager = moneyManager
        self._orderManager = orderManager
        self._riskManager = riskManager

        self.ibApi.attach(self)

    @property
    def contract(self):
        return self._contract
    
    @contract.setter
    def contract(self,value):
        pass

    @contract.deleter
    def contract(self):
        pass

    @abstractmethod
    def buy(self):
        pass

    @abstractmethod
    def sell(self):
        pass

    @abstractmethod
    def execute_stop(self):
        pass

    @abstractmethod
    def update(self,value):
        pass
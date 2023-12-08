from ibapi.client import *
from ibapi.wrapper import *

import logging
import os

logging.basicConfig(
    filename= os.path.join('..', 'debbug_app.log'),
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Wrapper(EWrapper):
    def __init__(self):
        EWrapper.__init__(self)

class Client(EClient):
    def __init__(self,wrapper):
        EClient.__init__(self,wrapper)

class App(Wrapper,Client):
    def __init__(self):
        Wrapper.__init__(self)
        Client.__init__(self,wrapper=self)
    
    def contractDetails(self, reqId: int, contractDetails: ContractDetails):
        logging.info(f"contract details: {contractDetails}")
        print(f"contract details: {contractDetails}")

    def contractDetailsEnd(self, reqId: int):
        logging.info("End of contractDetails")
        print("End of contractDetails")
        self.disconnect()
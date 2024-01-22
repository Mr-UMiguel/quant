from api.ibApi import IBApi
from controller.money_manager import MoneyManager
from controller.risk_manager import RiskManager
from controller.order_manager import OrderManager
from utils.contract_builder import create_contract
from model.mma_strategy import MMAStrategy



import logging
import traceback
import time
from threading import Thread

logging.basicConfig(filename='app.log',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

nu_info = {'symbol':'NU','secType':'STK','exchange':'SMART','currency':'USD'}

def main():

    #Instantiating app
    app = IBApi()

    ## contract
    mycontract =  create_contract(nu_info)

    ## managers
    moneyManager = MoneyManager(budget=100)
    riskManager = RiskManager()
    orderManager = OrderManager()

    ## Strategy
    mma = MMAStrategy(nperiods=4, ibApi = app, contract = mycontract,
                        moneyManager=moneyManager, riskManager=riskManager,
                        orderManager=orderManager)
    

    app.connect(host='127.0.0.1',port=7497,clientId=1)
    app.run()

    # time.sleep(5)
    reqId = app.nextOrderID
    app.reqMktData(reqId, contract=mma.contract)

    
    # app.cancelMktData(reqId)
    # app.disconnect()


if __name__ == "__main__":
    main()

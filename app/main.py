from ibapi.contract import Contract
from controller.market_data.ibHistMktData import IBHistMktData

from __init__ import App

import json
import time
import os

file_path = os.path.join('source', 'testMktData.json')
with open(file_path, 'w') as file:
        json.dump([], file, indent=4) 

def main():

    app = App()
    app.connect("127.0.0.1",7497,1000)

    
    # app.reqAccountSummary(12,groupName="All",tags='TotalCashValue')

    mycontract = Contract()
    mycontract.symbol = "AAPL"
    mycontract.secType = "STK"
    mycontract.exchange = "SMART"
    mycontract.currency = "USD"

    endDate = '20231208 16:31:00 US/Eastern'
    bRollOver = '2 D'
    bSize = '30 mins'
    wTS = 'TRADES'

    time.sleep(3)
    app.reqHistoricalData(1, mycontract, endDate, bRollOver, bSize, wTS, 1, 1, False, [])

    time.sleep(3)
    app.disconnect()
    app.run()
    
    
    


if __name__ == "__main__":
    main()

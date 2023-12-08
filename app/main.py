from ibapi.contract import Contract
# from controller.market_data.ibHistMktData import IBHistMktData

from __init__ import App

def main():

    app = App()
    app.connect("127.0.0.1",7497,1000)
    app.run()


    contract = Contract()
    contract.symbol = "AAPL"
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"
    start_date = "20231208 16:00:00 US/Eastern"
    broll_dates = "1 D"
    freq = "5 min"
    on = "TRADES"
    orderID = 1
    

    app.getData()

    print("done")

    


if __name__ == "__main__":
    main()
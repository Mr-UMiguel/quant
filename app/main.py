from ibapi.contract import Contract

from __init__ import App

def main():

    app = App()

    app.connect("127.0.0.1",7497,1000)

    contract = Contract()
    contract.symbol = "AAPL"
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"

    app.reqContractDetails(1,contract)
    app.run()


if __name__ == "__main__":
    main()
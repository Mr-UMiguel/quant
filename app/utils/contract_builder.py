from ibapi.wrapper import Contract

def create_contract(contract_info:dict):
    mycontract = Contract()
    mycontract.symbol = contract_info['symbol']
    mycontract.secType = contract_info['secType']
    mycontract.exchange = contract_info['exchange']
    mycontract.currency = contract_info['currency']
    return mycontract

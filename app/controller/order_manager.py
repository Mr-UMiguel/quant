from ibapi.client import Order
from typing import Literal
class OrderManager:
    @staticmethod
    def create_lmt_order(reqId:int, action: Literal["BUY","SELL"],
                            lmtPrice:float, totalQty:int):
        
        myorder = Order()
        myorder.orderId = reqId
        myorder.action = action
        myorder.tif = "GTC"
        myorder.orderType = "LMT"
        myorder.lmtPrice = lmtPrice
        myorder.totalQuantity = totalQty

        return myorder
    @staticmethod
    def create_mkt_order(reqId:int, action:Literal["BUY","SELL"], 
                            totalQty:int):
        
        myorder = Order()
        myorder.orderId = reqId
        myorder.action = action
        myorder.orderType = "MKT"
        myorder.totalQuantity = totalQty

        return myorder
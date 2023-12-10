from .strategy import Strategy
import numpy as np

class MMAStrategy(Strategy):

    def __init__(self,nperiods:int):
        self.nperiods = nperiods
        self.vprices = []
        super().__init__()

    def buy(self,mma,px):
        print(f"Buy mma:{mma} px:{px}")
        pass

    def sell(self):
        print("Sell")
        pass

    def clc_mma(self,value:float):
        if len(self.vprices)<self.nperiods:
            self.vprices.append(value)
            return value
        else:
            self.vprices.pop(0)
            self.vprices.append(value)
            return round(sum(self.vprices)/self.nperiods,2)


    def update(self,barData:float):
        px = float(barData['close'])
        mma = self.clc_mma(px)
        if px < mma:
            self.buy(mma,px)


from controller.strategy_manager import Strategy

class MMAStrategy(Strategy):

    def __init__(self,nperiods:int,**kwargs):
        self.nperiods = nperiods
        self.vprices = []
        Strategy.__init__(self,**kwargs)

    def buy(self,px):
        print(f"Buy - {px}")
        

    def sell(self):
        print("Sell")
        pass

    def execute_stop(self):
        pass

    def clc_mma(self,value:float):
        if len(self.vprices)<self.nperiods:
            self.vprices.append(value)
            return value
        else:
            self.vprices.pop(0)
            self.vprices.append(value)
            return round(sum(self.vprices)/self.nperiods,2)


    def update(self,value):
        px = value['price']
        mma = self.clc_mma(px)
        print(f"px: {px}, mma:{mma}")
        if px < mma:
            future = self.ibApi.executor.submit(self.buy,px)
            self.ibApi._futures.update({'buy': future})

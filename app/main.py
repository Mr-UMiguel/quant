from api.ibApp import IBApp
from model.mma_strategy import MMAStrategy
import numpy as np
def main():
    app = IBApp()
    barData = app.get_testVPrices()
    mma = MMAStrategy(nperiods= 20)

    app.attach(mma)
    app.sim_rtData(barData)
    
if __name__ == "__main__":
    main()

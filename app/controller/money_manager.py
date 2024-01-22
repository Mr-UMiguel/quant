class MoneyManager:
    _instance = None
    _initialized = False
    _cash_onhand = None
    def __init__(self,budget:float):
        if not self._initialized:
            self._budget = budget
            self._cash_onhand = self._budget
            self._initialized = True

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self,value):
        pass

    @budget.deleter
    def budget(self):
        pass

    @property
    def availablecash(self):
        return self._cash_onhand
    
    @availablecash.setter
    def availablecash(self, value:float):
        pass
    
    @availablecash.deleter
    def availablecash(self):
        pass

    def withdraw_money(self,amount:float):
        if amount > 0:
            if amount <= self._cash_onhand:
                self._cash_onhand -= amount
            else:
                pass

    def deposit_money(self,amount:float):
        if amount > 0:
            self._cash_onhand += amount

    def __new__(cls,*args,**kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
        
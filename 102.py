class Phone:
    def __init__(self):
        self.brand="apple"
        self.__price=13000#başta __ var sonda yoksa encapsilation
    def sell(self):
        print(f"prices {self.__price}")
    def sellprice(self,price):
        self.price = price
        print(f"artık fiyatı {price}")
obj=Phone()
obj.sell()
obj.sellprice(11000)
obj.sellprice(14000)
obj.sell()

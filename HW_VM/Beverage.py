class Beverage:
    def __init__(self, name, price, count):
        self.__name = name
        self.__price = price
        self.__count = count
        self.__salesCount = 0

    def ChangePrice(self, price):
        self.__price = price

    def ChangeCount(self, count):
        self.__count = count

    def InsertCount(self, count):
        self.__count += count

    def ExtractCount(self, count):
        self.__count -= count

    def ChangeName(self, name):
        self.__name = name

    def GetName(self):
        return self.__name

    def GetPrice(self):
        return self.__price

    def GetCount(self):
        return self.__count

    def GetSales(self, count = 1):
        self.__count -= count
        self.__salesCount += count
class Product:
    def __init__(self, name, price, count):
        self._name = name
        self._price = price
        self._count = count
        self._salesCount = 0

    def GetName(self):
        return self._name

    def GetPrice(self):
        return self._price

    def GetCount(self):
        return self._count

    def GetSales(self):
        return self._salesCount

    def Sales(self,count = 1):
        self._count -= count
        self._salesCount += count

    def ResetSales(self):
        self._salesCount = 0
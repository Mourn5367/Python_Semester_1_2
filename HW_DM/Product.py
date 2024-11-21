
class Product:
    def __init__(self, name, price, count):
        self._name = name
        self._price = price
        self._count = count

    def GetName(self):
        return self._name

    def GetPrice(self):
        return self._price

    def GetCount(self):
        return self._count
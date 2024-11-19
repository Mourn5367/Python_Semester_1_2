
class Product:
    def __init__(self, name, price, count):
        self._name = name
        self._price = price
        self._count = count

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price
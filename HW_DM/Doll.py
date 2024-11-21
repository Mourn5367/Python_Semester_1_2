from HW_DM.Product import Product


class Doll(Product):
    def __init__(self, name, price,count,position:list):
        super().__init__(name, price,count)
        self.__position = position


    def InsertCount(self, count):
        self._count += count

    def ExtractCount(self, count = 1):
        self._count -= count


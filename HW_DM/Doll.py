from HW_DM.Product import Product


class Doll(Product):
    def __init__(self, name, price,count,salesCount,position:list):
        super().__init__(name, price,count)
        self.__salesCount = salesCount
        self.__position = position

    def ChangeCount(self, count):
        self.__count = count

    def InsertCount(self, count):
        self.__count += count

    def ExtractCount(self, count = 1):
        self.__count -= count

    def Sales(self,count):
        self.__count -= count
        self.__salesCount += count

    def GetSales(self):
        return self.__salesCount

    def ResetSales(self):
        self.__salesCount = 0
from HW_DM.Product import Product


class Doll(Product):
    def __init__(self, name, price,count,position:list,imgPath):
        super().__init__(name, price,count)
        self.__position = position
        self.__imgPath = imgPath


    def InsertCount(self, count):
        self._count += count

    def ExtractCount(self, count = 1):
        self._count -= count

    def GetPosition(self):
        return self.__position

    def SetPosition(self, position):
        self.__position = position

    def GetImgPath(self):
        return self.__imgPath

    @staticmethod
    def GetSize():
        return 2

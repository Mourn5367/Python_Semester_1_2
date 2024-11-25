from HM_NEW_DM.Product import Product


class Doll(Product):
    def __init__(self, name, price,count,position:int,imgPath):
        super().__init__(name, price,count)
        self.__position = position
        self.__imgPath = imgPath

    def GetPosition(self):
        return self.__position

    def SetPosition(self, position):
        self.__position = position

    def GetImgPath(self):
        return self.__imgPath

    @staticmethod
    def GetSize():
        return 2



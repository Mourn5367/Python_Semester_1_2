from PIL import Image
class Claw:
    def __init__(self):
        self.__w = 0
        self.__h = 8
        self.size = [2,2]
        self.imgPath = Image.open("clawImg/claw.webp")

    def SetW(self, w:int):
        self.__w = w
    def SetH(self, h:int):
        self.__h = h
    def GetSize(self):
        return self.size
    def GetImgPath(self):
        return self.imgPath
    def GetW(self):
        return self.__w
    def GetH(self):
        return self.__h
    def RestW(self):
        self.__w = 0

